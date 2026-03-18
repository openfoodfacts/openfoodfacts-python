import dataclasses
import logging
import warnings

import albumentations as A
import numpy as np
from tritonclient.grpc import service_pb2

from openfoodfacts.ml.triton import (
    add_triton_infer_input_tensor,
    get_triton_inference_stub,
)
from openfoodfacts.utils import PerfTimer

logger = logging.getLogger(__name__)


@dataclasses.dataclass
class ImageClassificationResult:
    """The result of an image classification model.

    Attributes:
        predictions (list[tuple[str, float]]): The list of label names and their
            corresponding confidence scores, ordered by confidence score in
            descending order.
        metrics (dict[str, float]): The performance metrics of the classification.
            Each key is the name of the metric (a step in the inference
            process), and the value is the time taken in seconds.
            The following metrics are provided:
                - preprocess_time: time taken to preprocess the image
                - grpc_request_build_time: time taken to build the gRPC request
                - triton_inference_time: time taken for Triton inference
                - postprocess_time: time taken to postprocess the results
    """

    predictions: list[tuple[str, float]]
    metrics: dict[str, float]


def _classify_transform(
    max_size: int,
    normalize_mean: tuple[float, float, float] = (0.0, 0.0, 0.0),
    normalize_std: tuple[float, float, float] = (1.0, 1.0, 1.0),
):
    return A.Compose(
        [
            A.LongestMaxSize(max_size=max_size, p=1.0),
            A.PadIfNeeded(min_height=max_size, min_width=max_size, p=1.0),
            A.ToRGB(p=1.0),
            A.Normalize(mean=normalize_mean, std=normalize_std, p=1.0),
        ]
    )


class ImageClassifier:
    def __init__(self, model_name: str, label_names: list[str], image_size: int = 224):
        """An image classifier based on Yolo models.

        We support models trained with Yolov8, v9, v10 and v11.

        :param model_name: the name of the model, as registered in Triton
        :param label_names: the list of label names
        :param image_size: the size of the input image for the model
        """
        self.model_name: str = model_name
        self.label_names = label_names
        self.image_size = image_size

    def predict(
        self,
        image: np.ndarray,
        triton_uri: str,
        model_version: str | None = None,
    ) -> ImageClassificationResult:
        """Run an image classification model on an image.

        The model is expected to have been trained with Ultralytics library
        (any Yolo classification model).

        :param image: the input NumPy array image
        :param triton_uri: URI of the Triton Inference Server, defaults to
            None. If not provided, the default value from settings is used.
        :param model_version: the version of the model to use, defaults to
            None. If not provided, the latest version is used.
        :return: the prediction results as an ImageClassificationResult
        """
        metrics: dict[str, float] = {}

        with PerfTimer("preprocess_time", metrics):
            image_array = self.preprocess(image)

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
            predictions = self.postprocess(response)

        return ImageClassificationResult(predictions=predictions, metrics=metrics)

    def preprocess(self, image: np.ndarray) -> np.ndarray:
        """Preprocess an image for object detection.

        :param image: the input NumPy array image
        :return: the preprocessed image as a NumPy array
        """
        with warnings.catch_warnings():
            warnings.filterwarnings("ignore", message="The image is already an RGB")
            image_array = _classify_transform(max_size=self.image_size)(image=image)[
                "image"
            ]
        image_array = np.transpose(image_array, (2, 0, 1))[np.newaxis, :]  # HWC to CHW
        return image_array

    def postprocess(
        self, response: service_pb2.ModelInferResponse
    ) -> list[tuple[str, float]]:
        """Postprocess the inference result.

        :param response: the inference response
        """
        if len(response.outputs) != 1:
            raise Exception(f"expected 1 output, got {len(response.outputs)}")

        if len(response.raw_output_contents) != 1:
            raise Exception(
                "expected 1 raw output content, got "
                f"{len(response.raw_output_contents)}"
            )

        output_index = {output.name: i for i, output in enumerate(response.outputs)}
        output = np.frombuffer(
            response.raw_output_contents[output_index["output0"]],
            dtype=np.float32,
        ).reshape((1, len(self.label_names)))[0]

        score_indices = np.argsort(-output)
        return [(self.label_names[i], float(output[i])) for i in score_indices]
