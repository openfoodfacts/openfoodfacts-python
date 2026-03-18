from PIL import Image

from openfoodfacts.ml.utils import resize_image


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
