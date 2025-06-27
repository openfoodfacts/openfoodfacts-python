import numpy as np
from PIL import Image

from openfoodfacts.ml.utils import convert_image_to_array, resize_image


class TestConvertImageToArray:
    def test_rgb(self):
        # Create a simple RGB image
        image = Image.new("RGB", (10, 10), color="red")
        array = convert_image_to_array(image)

        assert array.shape == (10, 10, 3)
        assert array.dtype == np.uint8
        assert (array == [255, 0, 0]).all()

    def test_non_rgb(self):
        # Create a simple grayscale image
        image = Image.new("L", (10, 10), color=128)
        array = convert_image_to_array(image)

        assert array.shape == (10, 10, 3)
        assert array.dtype == np.uint8
        assert (array == [128, 128, 128]).all()

    def test_size(self):
        # Create a simple RGB image with different size
        image = Image.new("RGB", (20, 15), color="blue")
        array = convert_image_to_array(image)

        assert array.shape == (15, 20, 3)
        assert array.dtype == np.uint8
        assert (array == [0, 0, 255]).all()


class TestResizeImage:
    def test_resize_smaller_image(self):
        # Create a simple RGB image smaller than max_size
        image = Image.new("RGB", (10, 10), color="red")
        max_size = (20, 20)
        resized_image = resize_image(image, max_size)

        assert resized_image.size == (10, 10)

    def test_resize_larger_image(self):
        # Create a simple RGB image larger than max_size
        image = Image.new("RGB", (30, 30), color="blue")
        max_size = (20, 20)
        resized_image = resize_image(image, max_size)

        assert resized_image.size == (20, 20)

    def test_resize_wider_image(self):
        # Create a simple RGB image wider than max_size
        image = Image.new("RGB", (40, 20), color="green")
        max_size = (20, 20)
        resized_image = resize_image(image, max_size)

        assert resized_image.size == (20, 10)

    def test_resize_taller_image(self):
        # Create a simple RGB image taller than max_size
        image = Image.new("RGB", (20, 40), color="yellow")
        max_size = (20, 20)
        resized_image = resize_image(image, max_size)

        assert resized_image.size == (10, 20)
