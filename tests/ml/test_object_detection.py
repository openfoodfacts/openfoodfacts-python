from unittest.mock import MagicMock, patch

import numpy as np
import pytest
from PIL import Image

from openfoodfacts.ml.object_detection import ObjectDetectionRawResult, ObjectDetector


@pytest.fixture
def sample_image():
    # Create a sample image for testing
    return Image.new("RGB", (100, 200), color="white")


@pytest.fixture
def object_detector():
    # Create an instance of ObjectDetector for testing
    label_names = ["label1", "label2"]
    return ObjectDetector(
        model_name="test_model", label_names=label_names, image_size=640
    )


class ResponseOutputs:
    def __init__(self, name):
        self.name = name


class TestObjectDetector:
    def test_preprocess(self, sample_image, object_detector):
        image_array, scale_x, scale_y = object_detector.preprocess(sample_image)

        # Check the shape of the output image array
        assert image_array.shape == (1, 3, 640, 640)

        # Check the scale factors
        # Here, image ratio (width / height) is 100 / 200 = 0.5
        assert scale_x == 640 * 0.5
        assert scale_y == 640

    def test_postprocess(self, object_detector):
        # Mock response object
        response = MagicMock()
        response.outputs = [ResponseOutputs("output0")]
        response.raw_output_contents = [
            np.random.rand(1, len(object_detector.label_names) + 4, 10)
            .astype(np.float32)
            .tobytes()
        ]

        threshold = 0.5
        scale_x = 1.0
        scale_y = 1.0

        result = object_detector.postprocess(response, threshold, scale_x, scale_y)

        # Check the type of the result
        assert isinstance(result, ObjectDetectionRawResult)

        # Check the number of detections
        assert result.num_detections == 10

        # Check the shape of detection boxes
        assert result.detection_boxes.shape == (len(result.detection_scores), 4)

        # Check the length of detection classes and scores
        assert len(result.detection_classes) == len(result.detection_scores)

    def test_detect_from_image(self, sample_image, object_detector):
        # Mock the Triton inference stub and response
        grpc_stub = MagicMock()
        grpc_stub.ModelInfer.return_value = MagicMock()
        get_triton_inference_stub = MagicMock(return_value=grpc_stub)

        # Mock the preprocess and postprocess methods
        object_detector.preprocess = MagicMock(
            return_value=(np.zeros((1, 3, 640, 640)), 1.0, 1.0)
        )
        object_detector.postprocess = MagicMock(
            return_value=ObjectDetectionRawResult(
                num_detections=1,
                detection_boxes=np.zeros((1, 4)),
                detection_scores=np.array([0.9]),
                detection_classes=np.array([1]),
                label_names=object_detector.label_names,
            )
        )
        with patch(
            "openfoodfacts.ml.object_detection.get_triton_inference_stub",
            get_triton_inference_stub,
        ):
            # Run the detect_from_image method
            result = object_detector.detect_from_image(
                sample_image, "fake_triton_uri", threshold=0.5
            )

        # Check that preprocess was called
        object_detector.preprocess.assert_called_once_with(sample_image)

        # Check that get_triton_inference_stub was called
        get_triton_inference_stub.assert_called_once_with("fake_triton_uri")

        # Check that ModelInfer was called
        grpc_stub.ModelInfer.assert_called_once()

        # Check that postprocess was called
        object_detector.postprocess.assert_called_once()

        # Check the type of the result
        assert isinstance(result, ObjectDetectionRawResult)

        # Check the number of detections
        assert result.num_detections == 1
