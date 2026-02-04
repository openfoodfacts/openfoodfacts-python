from unittest.mock import MagicMock, patch

import numpy as np
import pytest
from PIL import Image

from openfoodfacts.ml.object_detection import (
    ObjectDetectionRawResult,
    ObjectDetector,
    apply_nms,
)


@pytest.fixture
def sample_image():
    # Create a sample image (np uint8 array) for testing
    return np.array(Image.new("RGB", (100, 200), color="white"))


@pytest.fixture
def object_detector() -> ObjectDetector:
    # Create an instance of ObjectDetector for testing
    label_names = ["label1", "label2"]
    return ObjectDetector(
        model_name="test_model", label_names=label_names, image_size=640
    )


class ResponseOutputs:
    def __init__(self, name):
        self.name = name


class TestObjectDetector:
    def test_preprocess(self, sample_image, object_detector: ObjectDetector):
        image_array = object_detector.preprocess(sample_image)

        # Check the shape of the output image array
        assert image_array.shape == (1, 3, 640, 640)

    def test_postprocess(self, object_detector: ObjectDetector):
        # Mock response object
        response = MagicMock()
        response.outputs = [ResponseOutputs("output0")]
        response.raw_output_contents = [
            np.random.rand(1, len(object_detector.label_names) + 4, 10)
            .astype(np.float32)
            .tobytes()
        ]

        threshold = 0.5
        result = object_detector.postprocess(
            response, threshold, original_shape=(200, 100)
        )

        # Check the type of the result
        assert isinstance(result, ObjectDetectionRawResult)

        # Check the number of detections
        assert result.num_detections == 10

        # Check the shape of detection boxes
        assert result.detection_boxes.shape == (len(result.detection_scores), 4)

        # Check the length of detection classes and scores
        assert len(result.detection_classes) == len(result.detection_scores)

    def test_detect_from_image(self, sample_image, object_detector: ObjectDetector):
        # Mock the Triton inference stub and response
        grpc_stub = MagicMock()
        grpc_stub.ModelInfer.return_value = MagicMock()
        get_triton_inference_stub = MagicMock(return_value=grpc_stub)

        # Mock the preprocess and postprocess methods
        object_detector.preprocess = MagicMock(return_value=np.zeros((1, 3, 640, 640)))  # type: ignore
        object_detector.postprocess = MagicMock(  # type: ignore
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
        object_detector.preprocess.assert_called_once()
        assert object_detector.preprocess.call_args.kwargs == {
            "image_array": sample_image
        }

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


class TestApplyNMS:
    """Unit tests for the apply_nms function."""

    threshold = 0.5
    nms_threshold = 0.5
    nms_eta = 1.0

    def test_basic_nms_single_box(self):
        """Test NMS with a single bounding box - should return unchanged."""
        bboxes = np.array([[0.1, 0.1, 0.5, 0.5]], dtype=np.float32)
        scores = np.array([0.9], dtype=np.float32)
        classes = np.array([0], dtype=int)

        result_boxes, result_scores, result_classes = apply_nms(
            bboxes=bboxes,
            scores=scores,
            classes=classes,
            threshold=self.threshold,
            nms_threshold=self.nms_threshold,
            nms_eta=self.nms_eta,
        )

        np.testing.assert_array_almost_equal(result_boxes, bboxes)
        np.testing.assert_array_almost_equal(result_scores, scores)
        np.testing.assert_array_equal(result_classes, classes)

    def test_nms_removes_overlapping_boxes_same_class(self):
        """Test that NMS removes overlapping boxes."""
        # Two highly overlapping boxes
        bboxes = np.array(
            [
                [0.1, 0.1, 0.5, 0.5],  # Original box
                [0.12, 0.12, 0.52, 0.52],  # Highly overlapping, should be suppressed
            ],
            dtype=np.float32,
        )
        scores = np.array([0.9, 0.8], dtype=np.float32)
        classes = np.array([0, 0], dtype=int)

        result_boxes, result_scores, result_classes = apply_nms(
            bboxes=bboxes,
            scores=scores,
            classes=classes,
            threshold=self.threshold,
            nms_threshold=0.5,  # Threshold low enough to suppress overlapping boxes
            nms_eta=self.nms_eta,
        )

        # Should only keep the higher score box
        assert len(result_boxes) == 1
        np.testing.assert_array_almost_equal(result_boxes[0], bboxes[0])
        assert result_scores[0] == scores[0]
        assert result_classes[0] == classes[0]

    def test_nms_keeps_non_overlapping_boxes(self):
        """Test that NMS keeps non-overlapping boxes."""
        bboxes = np.array(
            [
                [0.1, 0.1, 0.3, 0.3],  # Top-left box
                [0.6, 0.6, 0.9, 0.9],  # Bottom-right box, no overlap
            ],
            dtype=np.float32,
        )
        scores = np.array([0.9, 0.85], dtype=np.float32)
        classes = np.array([0, 0], dtype=int)

        result_boxes, result_scores, result_classes = apply_nms(
            bboxes=bboxes,
            scores=scores,
            classes=classes,
            threshold=self.threshold,
            nms_threshold=0.5,
            nms_eta=self.nms_eta,
        )

        # Should keep both boxes
        assert len(result_boxes) == 2
        np.testing.assert_array_almost_equal(result_boxes, bboxes)
        np.testing.assert_array_almost_equal(result_scores, scores)
        np.testing.assert_array_equal(result_classes, classes)

    def test_apply_nms_filters_by_threshold(self):
        """Test that boxes below confidence threshold are filtered out."""
        bboxes = np.array(
            [
                [0.1, 0.1, 0.5, 0.5],  # Above threshold
                [0.6, 0.6, 0.9, 0.9],  # Below threshold
            ],
            dtype=np.float32,
        )
        scores = np.array([0.6, 0.3], dtype=np.float32)  # 0.3 < threshold=0.5
        classes = np.array([0, 0], dtype=int)

        result_boxes, result_scores, result_classes = apply_nms(
            bboxes=bboxes,
            scores=scores,
            classes=classes,
            threshold=self.threshold,
            nms_threshold=self.nms_threshold,
            nms_eta=self.nms_eta,
        )

        # Should only keep the box above threshold
        assert len(result_boxes) == 1
        np.testing.assert_array_almost_equal(result_boxes[0], bboxes[0])
        np.testing.assert_array_almost_equal(result_scores[0], scores[0])

    def test_apply_nms_empty_input(self):
        """Test NMS with no input boxes."""
        bboxes = np.zeros((0, 4), dtype=np.float32)
        scores = np.zeros(0, dtype=np.float32)
        classes = np.zeros(0, dtype=int)

        result_boxes, result_scores, result_classes = apply_nms(
            bboxes=bboxes,
            scores=scores,
            classes=classes,
            threshold=self.threshold,
            nms_threshold=self.nms_threshold,
            nms_eta=self.nms_eta,
        )

        assert len(result_boxes) == 0
        assert len(result_scores) == 0
        assert len(result_classes) == 0

    def test_apply_nms_all_below_threshold(self):
        """Test NMS when all boxes are below confidence threshold."""
        bboxes = np.array(
            [
                [0.1, 0.1, 0.5, 0.5],
                [0.6, 0.6, 0.9, 0.9],
            ],
            dtype=np.float32,
        )
        scores = np.array([0.3, 0.4], dtype=np.float32)  # Both below 0.5
        classes = np.array([0, 0], dtype=int)

        result_boxes, result_scores, result_classes = apply_nms(
            bboxes=bboxes,
            scores=scores,
            classes=classes,
            threshold=self.threshold,
            nms_threshold=self.nms_threshold,
            nms_eta=self.nms_eta,
        )

        assert len(result_boxes) == 0
        assert len(result_scores) == 0
        assert len(result_classes) == 0

    def test_nms_keeps_highest_score_in_cluster(self):
        """Test that NMS keeps highest scoring box in a cluster of overlaps."""
        # Three overlapping boxes, middle score should be suppressed
        bboxes = np.array(
            [
                [0.1, 0.1, 0.6, 0.6],  # Lowest score, should be suppressed
                [0.1, 0.1, 0.5, 0.5],  # Highest score, should be kept
                [0.1, 0.1, 0.55, 0.55],  # Middle score, should be suppressed
            ],
            dtype=np.float32,
        )
        scores = np.array([0.7, 0.95, 0.8], dtype=np.float32)
        classes = np.array([0, 0, 0], dtype=int)

        result_boxes, result_scores, result_classes = apply_nms(
            bboxes=bboxes,
            scores=scores,
            classes=classes,
            threshold=self.threshold,
            nms_threshold=0.5,
            nms_eta=self.nms_eta,
        )

        # Should at least keep the highest scoring box
        assert len(result_boxes) == 1
        np.testing.assert_array_almost_equal(
            result_boxes, np.array([[0.1, 0.1, 0.5, 0.5]])
        )
        assert result_scores[0] == 0.95
        assert result_classes[0] == 0

    def test_bbbox_format_conversion(self):
        """Test that bbox format conversion is correct (y_min,x_min,y_max,x_max) -> (x,y,w,h)."""
        # This test verifies the internal conversion in apply_nms
        bboxes = np.array([[0.0, 0.0, 1.0, 1.0]], dtype=np.float32)  # Full image
        scores = np.array([1.0], dtype=np.float32)
        classes = np.array([0], dtype=int)

        result_boxes, result_scores, result_classes = apply_nms(
            bboxes=bboxes,
            scores=scores,
            classes=classes,
            threshold=0.0,  # Include all
            nms_threshold=0.5,
            nms_eta=self.nms_eta,
        )

        # Output should preserve original format
        np.testing.assert_array_almost_equal(result_boxes, bboxes)

    def test_multiple_detections_per_class(self):
        """Test NMS with multiple separate detections of the same class."""
        bboxes = np.array(
            [
                [0.0, 0.0, 0.3, 0.3],  # Detection 1, class 0
                [0.5, 0.5, 0.8, 0.8],  # Detection 2, class 0 (no overlap with 1)
                [0.0, 0.5, 0.3, 0.8],  # Detection 3, class 0 (no overlap)
            ],
            dtype=np.float32,
        )
        scores = np.array([0.9, 0.85, 0.8], dtype=np.float32)
        classes = np.array([0, 0, 0], dtype=int)

        result_boxes, result_scores, result_classes = apply_nms(
            bboxes=bboxes,
            scores=scores,
            classes=classes,
            threshold=self.threshold,
            nms_threshold=0.5,
            nms_eta=self.nms_eta,
        )

        # All three should be kept since they don't overlap
        assert len(result_boxes) == 3

    def test_nms_threshold_extremes(self):
        """Test NMS with extreme threshold values."""
        bboxes = np.array(
            [
                [0.1, 0.1, 0.5, 0.5],
                [0.12, 0.12, 0.52, 0.52],  # Highly overlapping
            ],
            dtype=np.float32,
        )
        scores = np.array([0.9, 0.8], dtype=np.float32)
        classes = np.array([0, 0], dtype=int)

        # Very high NMS threshold (0.99) - less suppression, keep both
        result_high, _, _ = apply_nms(
            bboxes=bboxes.copy(),
            scores=scores.copy(),
            classes=classes.copy(),
            threshold=self.threshold,
            nms_threshold=0.99,
            nms_eta=self.nms_eta,
        )

        # Very low NMS threshold (0.1) - more suppression
        result_low, _, _ = apply_nms(
            bboxes=bboxes.copy(),
            scores=scores.copy(),
            classes=classes.copy(),
            threshold=self.threshold,
            nms_threshold=0.01,
            nms_eta=self.nms_eta,
        )

        assert len(result_high) == 2
        assert len(result_low) == 1

    def test_return_type_correctness(self):
        """Test that return types are correct."""
        bboxes = np.array([[0.1, 0.1, 0.5, 0.5]], dtype=np.float32)
        scores = np.array([0.9], dtype=np.float32)
        classes = np.array([0], dtype=int)

        result_boxes, result_scores, result_classes = apply_nms(
            bboxes=bboxes,
            scores=scores,
            classes=classes,
            threshold=self.threshold,
            nms_threshold=self.nms_threshold,
            nms_eta=self.nms_eta,
        )

        assert isinstance(result_boxes, np.ndarray)
        assert isinstance(result_scores, np.ndarray)
        assert isinstance(result_classes, np.ndarray)
        assert result_boxes.dtype == np.float32
        assert result_scores.dtype == np.float32
        assert result_classes.dtype == int
        assert result_boxes.shape[1] == 4  # (N, 4) shape

    def test_nms_eta_effect(self):
        """Test that nms_eta parameter is passed correctly."""
        bboxes = np.array(
            [
                [0.1, 0.1, 0.5, 0.5],
                [0.2, 0.2, 0.6, 0.6],
            ],
            dtype=np.float32,
        )
        scores = np.array([0.9, 0.8], dtype=np.float32)
        classes = np.array([0, 0], dtype=int)

        # Different eta values
        result_eta_1, _, _ = apply_nms(
            bboxes=bboxes.copy(),
            scores=scores.copy(),
            classes=classes.copy(),
            threshold=self.threshold,
            nms_threshold=0.5,
            nms_eta=1.0,
        )

        result_eta_05, _, _ = apply_nms(
            bboxes=bboxes.copy(),
            scores=scores.copy(),
            classes=classes.copy(),
            threshold=self.threshold,
            nms_threshold=0.5,
            nms_eta=0.5,
        )

        # Just verify they run without error and return valid shapes
        assert result_eta_1.shape[1] == 4
        assert result_eta_05.shape[1] == 4
