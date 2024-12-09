from unittest.mock import MagicMock, patch

import numpy as np
from PIL import Image

from openfoodfacts.ml.image_classification import ImageClassifier, classify_transforms


class TestClassifyTransforms:
    def test_rgb_image(self):
        img = Image.new("RGB", (300, 300), color="red")
        transformed_img = classify_transforms(img)
        assert transformed_img.shape == (3, 224, 224)
        assert transformed_img.dtype == np.float32

    def test_non_rgb_image(self):
        img = Image.new("L", (300, 300), color="red")
        transformed_img = classify_transforms(img)
        assert transformed_img.shape == (3, 224, 224)
        assert transformed_img.dtype == np.float32

    def test_custom_size(self):
        img = Image.new("RGB", (300, 300), color="red")
        transformed_img = classify_transforms(img, size=128)
        assert transformed_img.shape == (3, 128, 128)
        assert transformed_img.dtype == np.float32

    def test_custom_mean_std(self):
        img = Image.new("RGB", (300, 300), color="red")
        mean = (0.5, 0.5, 0.5)
        std = (0.5, 0.5, 0.5)
        transformed_img = classify_transforms(img, mean=mean, std=std)
        assert transformed_img.shape == (3, 224, 224)
        assert transformed_img.dtype == np.float32

    def test_custom_interpolation(self):
        img = Image.new("RGB", (300, 300), color="red")
        transformed_img = classify_transforms(
            img, interpolation=Image.Resampling.NEAREST
        )
        assert transformed_img.shape == (3, 224, 224)
        assert transformed_img.dtype == np.float32

    def test_custom_crop_fraction(self):
        img = Image.new("RGB", (300, 300), color="red")
        transformed_img = classify_transforms(img, crop_fraction=0.8)
        assert transformed_img.shape == (3, 224, 224)
        assert transformed_img.dtype == np.float32


class ResponseOutputs:
    def __init__(self, name):
        self.name = name


class TestImageClassifier:
    def test_preprocess_rgb_image(self):
        img = Image.new("RGB", (300, 300), color="red")
        classifier = ImageClassifier(
            model_name="test_model", label_names=["label1", "label2"]
        )
        preprocessed_img = classifier.preprocess(img)
        assert preprocessed_img.shape == (1, 3, 224, 224)
        assert preprocessed_img.dtype == np.float32

    def test_postprocess_single_output(self):
        classifier = ImageClassifier(
            model_name="test_model", label_names=["label1", "label2"]
        )
        response = MagicMock()
        response.outputs = [ResponseOutputs(name="output0")]
        response.raw_output_contents = [
            np.array([0.8, 0.2], dtype=np.float32).tobytes()
        ]

        result = classifier.postprocess(response)
        assert len(result) == 2
        assert result[0][0] == "label1"
        assert np.isclose(result[0][1], 0.8)
        assert result[1][0] == "label2"
        assert np.isclose(result[1][1], 0.2)

    def test_postprocess_multiple_outputs(self):
        classifier = ImageClassifier(
            model_name="test_model", label_names=["label1", "label2"]
        )
        response = MagicMock()
        response.outputs = [
            ResponseOutputs(name="output0"),
            ResponseOutputs(name="output1"),
        ]
        response.raw_output_contents = [
            np.array([0.8, 0.2], dtype=np.float32).tobytes()
        ]

        try:
            classifier.postprocess(response)
        except Exception as e:
            assert str(e) == "expected 1 output, got 2"

    def test_postprocess_multiple_raw_output_contents(self):
        classifier = ImageClassifier(
            model_name="test_model", label_names=["label1", "label2"]
        )
        response = MagicMock()
        response.outputs = [ResponseOutputs(name="output0")]
        response.raw_output_contents = [
            np.array([0.8, 0.2], dtype=np.float32).tobytes(),
            np.array([0.1, 0.9], dtype=np.float32).tobytes(),
        ]

        try:
            classifier.postprocess(response)
        except Exception as e:
            assert str(e) == "expected 1 raw output content, got 2"

    def test_predict(self):
        img = Image.new("RGB", (300, 300), color="red")
        classifier = ImageClassifier(
            model_name="test_model", label_names=["label1", "label2"]
        )
        triton_uri = "fake_triton_uri"

        # Mock the preprocess method
        classifier.preprocess = MagicMock(
            return_value=np.random.rand(1, 3, 224, 224).astype(np.float32)
        )

        # Mock the Triton inference stub and response
        grpc_stub = MagicMock()
        response = MagicMock()
        response.outputs = [ResponseOutputs(name="output0")]
        response.raw_output_contents = [
            np.array([0.8, 0.2], dtype=np.float32).tobytes()
        ]
        grpc_stub.ModelInfer = MagicMock(return_value=response)

        # Mock the get_triton_inference_stub function
        get_triton_inference_stub = MagicMock(return_value=grpc_stub)

        with patch(
            "openfoodfacts.ml.image_classification.get_triton_inference_stub",
            get_triton_inference_stub,
        ):
            result = classifier.predict(img, triton_uri)

        assert len(result) == 2
        assert result[0][0] == "label1"
        assert np.isclose(result[0][1], 0.8)
        assert result[1][0] == "label2"
        assert np.isclose(result[1][1], 0.2)

        classifier.preprocess.assert_called_once_with(img)
        grpc_stub.ModelInfer.assert_called_once()
        get_triton_inference_stub.assert_called_once_with(triton_uri)
