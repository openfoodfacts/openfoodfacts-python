import dataclasses
import logging
import typing

import albumentations as A
import cv2
import numpy as np
from cv2 import dnn
from tritonclient.grpc import service_pb2

from openfoodfacts.types import JSONType
from openfoodfacts.utils import PerfTimer

from .triton import add_triton_infer_input_tensor, get_triton_inference_stub

logger = logging.getLogger(__name__)


def object_detection_transform(
    image_size: int,
    fill: int = 114,
    pad_position: str = "center",
    normalize_mean: tuple[float, float, float] = (0.0, 0.0, 0.0),
    normalize_std: tuple[float, float, float] = (1.0, 1.0, 1.0),
) -> A.Compose:
    """Return the Albumentations transform pipeline for object detection.

    It resizes the image to fit within a square of size (image_size,
    image_size), preserving the aspect ratio, then pads the image to make it
    square, and finally normalizes the image.

    With the default settings, this pipeline matches the preprocessing used by
    Ultralytics YOLO models.

    Args:
        image_size (int): The target size for the longest side of the image.
        fill (int): The pixel value to use for padding. Default is 114.
        pad_position (str): The position to place the original image when
                            padding. Default is "center".
        normalize_mean (tuple): The mean values for normalization. Default is
                                (0.0, 0.0, 0.0).
        normalize_std (tuple): The std values for normalization. Default is
                               (1.0, 1.0, 1.0).
    """
    return A.Compose(
        [
            A.LongestMaxSize(max_size=image_size, interpolation=cv2.INTER_LINEAR),
            A.PadIfNeeded(
                min_height=image_size,
                min_width=image_size,
                position=pad_position,
                fill=fill,
            ),
            A.Normalize(mean=normalize_mean, std=normalize_std, p=1.0),
        ],
    )


def reverse_bbox_transform(
    augmented_bbox: list, original_shape: tuple, image_size: int
) -> list:
    """
    Reverses the Albumentations pipeline to find original bbox coordinates.

    Args:
        augmented_bbox (list): [y_min, x_min, y_max, x_max] from the
                               augmented (image_size x image_size) image.
        original_shape (tuple): (height, width) of the *original* image.
        image_size (int): The target size used in the pipeline.

    Returns:
        list: [y_min, x_min, y_max, x_max] in relative coordinates.
    """

    original_h, original_w = original_shape

    # --- 1. Re-calculate the forward transform parameters ---

    # From A.LongestMaxSize
    scale = image_size / max(original_h, original_w)

    # The dimensions of the image *after* scaling but *before* padding
    scaled_h = int(original_h * scale)
    scaled_w = int(original_w * scale)

    # From A.PadIfNeeded (position="center")
    # This is the amount of padding added to each side
    pad_top = (image_size - scaled_h) // 2
    pad_left = (image_size - scaled_w) // 2

    # --- 2. Apply the inverse transformation ---
    aug_y_min, aug_x_min, aug_y_max, aug_x_max = augmented_bbox

    # coord_orig = (coord_aug - padding) / scale
    orig_y_min = (aug_y_min - pad_top) / scale
    orig_x_min = (aug_x_min - pad_left) / scale
    orig_y_max = (aug_y_max - pad_top) / scale
    orig_x_max = (aug_x_max - pad_left) / scale

    return [
        orig_y_min / original_h,
        orig_x_min / original_w,
        orig_y_max / original_h,
        orig_x_max / original_w,
    ]


@dataclasses.dataclass
class ObjectDetectionRawResult:
    """The raw result of an object detection model.

    Attributes:
        num_detections (int): The number of detections.
        detection_boxes (np.ndarray): The bounding boxes of the detections, in
            relative coordinates (between 0 and 1), with the format
            (y_min, x_min, y_max, x_max).
        detection_scores (np.ndarray): The scores of the detections.
        detection_classes (np.ndarray): The class indices of the detections.
        label_names (list[str]): The list of label names.
        metrics (dict[str, float]): The performance metrics of the detection.
            Each key is the name of the metric (a step in the inference
            process), and the value is the time taken in seconds.
            The following metrics are provided:
                - preprocess_time: time taken to preprocess the image
                - grpc_request_build_time: time taken to build the gRPC request
                - triton_inference_time: time taken for Triton inference
                - postprocess_time: time taken to postprocess the results
                - postprocess_nms_time: time taken for Non-Maximum Suppression
                  (included in postprocess_time)
    """

    num_detections: int
    detection_boxes: np.ndarray
    detection_scores: np.ndarray
    detection_classes: np.ndarray
    label_names: list[str]
    metrics: dict[str, float] = dataclasses.field(default_factory=dict)

    def to_list(self) -> list[JSONType]:
        """Convert the detection results to a JSON serializable format."""
        results = []
        for bounding_box, score, label in zip(
            self.detection_boxes, self.detection_scores, self.detection_classes
        ):
            label_int = int(label)
            label_str = self.label_names[label_int]
            if label_str is not None:
                result = {
                    "bounding_box": tuple(bounding_box.tolist()),  # type: ignore
                    "score": float(score),
                    "label": label_str,
                }
                results.append(result)
        return results


class ObjectDetector:
    def __init__(self, model_name: str, label_names: list[str], image_size: int = 640):
        """An object detection detector based on Yolo models.

        We support models trained with Yolov8, v9, v10, v11 and v12 from
        Ultralytics.

        :param model_name: the name of the model, as registered in Triton
        :param label_names: the list of label names
        :param image_size: the size of the input image for the model
        """
        self.model_name: str = model_name
        self.label_names = label_names
        self.image_size = image_size

    def detect_from_image(
        self,
        image: np.ndarray,
        triton_uri: str,
        threshold: float = 0.5,
        nms_threshold: float | None = None,
        nms_eta: float | None = None,
        model_version: str | None = None,
    ) -> ObjectDetectionRawResult:
        """Run an object detection model on an image.

        The model must have been trained with Ultralytics library.

        :param image: the input numpy image
        :param triton_uri: URI of the Triton Inference Server, defaults to
            None. If not provided, the default value from settings is used.
        :param threshold: the minimum score for a detection to be considered,
            defaults to 0.5.
        :param nms_threshold: the NMS (Non Maximum Suppression) threshold to
            use, defaults to None (0.7 will be used).
        :param nms_eta: the NMS eta parameter to use, defaults to None (1.0
            will be used).
        :param model_version: the version of the model to use, defaults to
            None (latest).
        :return: the detection result
        """
        metrics: dict[str, float] = {}

        with PerfTimer("preprocess_time", metrics):
            image_array = self.preprocess(image_array=image)

        with PerfTimer("grpc_request_build_time", metrics):
            request = service_pb2.ModelInferRequest()
            request.model_name = self.model_name
            if model_version:
                request.model_version = model_version
            add_triton_infer_input_tensor(
                request, name="images", data=image_array, datatype="FP32"
            )

        with PerfTimer("triton_inference_time", metrics):
            grpc_stub = get_triton_inference_stub(triton_uri)
            response = grpc_stub.ModelInfer(request)

        with PerfTimer("postprocess_time", metrics):
            original_shape = typing.cast(tuple[int, int], image.shape[:2])
            response = self.postprocess(
                response,
                threshold=threshold,
                original_shape=original_shape,
                nms_threshold=nms_threshold,
                nms_eta=nms_eta,
            )

        metrics.update(response.metrics)
        metrics["total_inference_time"] = (
            metrics["preprocess_time"]
            + metrics["grpc_request_build_time"]
            + metrics["triton_inference_time"]
            + metrics["postprocess_time"]
        )
        response.metrics = metrics
        return response

    def preprocess(self, image_array: np.ndarray) -> np.ndarray:
        # Apply the transform to the image
        image_array = object_detection_transform(image_size=self.image_size)(
            image=image_array
        )["image"]
        image_array = np.transpose(image_array, (2, 0, 1))[np.newaxis, :]  # HWC to CHW
        return image_array

    def postprocess(
        self,
        response,
        threshold: float,
        original_shape: tuple[int, int],
        nms_threshold: float | None = None,
        nms_eta: float | None = None,
    ) -> ObjectDetectionRawResult:
        """Postprocess the output of the object detection model.

        :param response: the Triton Inference response
        :param threshold: the minimum score for a detection to be considered
        :param original_shape: the original shape of the image (height, width)
        :param nms_threshold: the NMS (Non Maximum Suppression) threshold to
            use, defaults to None (0.7 will be used).
        :param nms_eta: the NMS eta parameter to use, defaults to None (1.0
            will be used).
        :return: the detection result
        """
        if len(response.outputs) != 1:
            raise ValueError(f"expected 1 output, got {len(response.outputs)}")

        if len(response.raw_output_contents) != 1:
            raise ValueError(
                f"expected 1 raw output content, got {len(response.raw_output_contents)}"
            )

        if nms_threshold is None:
            nms_threshold = 0.7
        if nms_eta is None:
            nms_eta = 1.0

        output_index = {output.name: i for i, output in enumerate(response.outputs)}
        output = np.frombuffer(
            response.raw_output_contents[output_index["output0"]],
            dtype=np.float32,
        ).reshape((1, len(self.label_names) + 4, -1))[0]

        # output is of shape (num_classes + 4, num_detections)
        rows = output.shape[1]
        raw_detection_classes = np.zeros(rows, dtype=int)
        raw_detection_scores = np.zeros(rows, dtype=np.float32)
        raw_detection_boxes = np.zeros((rows, 4), dtype=np.float32)

        for i in range(rows):
            classes_scores = output[4:, i]
            max_cls_idx = np.argmax(classes_scores)
            max_score = classes_scores[max_cls_idx]
            if max_score < threshold:
                continue
            raw_detection_classes[i] = max_cls_idx
            raw_detection_scores[i] = max_score

            # The bounding box is in the format (x, y, width, height) in
            # relative coordinates
            # x and y are the coordinates of the center of the bounding box
            bbox_width = output[2, i]
            bbox_height = output[3, i]
            x_min = output[0, i] - 0.5 * bbox_width
            y_min = output[1, i] - 0.5 * bbox_height
            x_max = x_min + bbox_width
            y_max = y_min + bbox_height

            # We save the bounding box in the format
            # (y_min, x_min, y_max, x_max) in relative coordinates
            # Scale the bounding boxes back to the original image size

            reversed_bboxes = reverse_bbox_transform(
                augmented_bbox=[y_min, x_min, y_max, x_max],
                original_shape=original_shape,
                image_size=self.image_size,
            )
            raw_detection_boxes[i, 0] = max(0.0, min(1.0, reversed_bboxes[0]))
            raw_detection_boxes[i, 1] = max(0.0, min(1.0, reversed_bboxes[1]))
            raw_detection_boxes[i, 2] = max(0.0, min(1.0, reversed_bboxes[2]))
            raw_detection_boxes[i, 3] = max(0.0, min(1.0, reversed_bboxes[3]))

        metrics: dict[str, float] = {}
        with PerfTimer("postprocess_nms_time", metrics):
            # Perform NMS (Non Maximum Suppression)
            detection_box_indices = dnn.NMSBoxes(
                raw_detection_boxes,  # type: ignore
                raw_detection_scores,  # type: ignore
                score_threshold=threshold,
                # the following values are copied from Ultralytics settings
                nms_threshold=nms_threshold,
                eta=nms_eta,
            )
        detection_classes = np.zeros(len(detection_box_indices), dtype=int)
        detection_scores = np.zeros(len(detection_box_indices), dtype=np.float32)
        detection_boxes = np.zeros((len(detection_box_indices), 4), dtype=np.float32)

        for i, idx in enumerate(detection_box_indices):
            detection_classes[i] = raw_detection_classes[idx]
            detection_scores[i] = raw_detection_scores[idx]
            detection_boxes[i] = raw_detection_boxes[idx]

        result = ObjectDetectionRawResult(
            num_detections=rows,
            detection_classes=detection_classes,
            detection_boxes=detection_boxes,
            detection_scores=detection_scores,
            label_names=self.label_names,
            metrics=metrics,
        )
        return result
