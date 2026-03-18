from PIL import Image


def resize_image(image: Image.Image, max_size: tuple[int, int]) -> Image.Image:
    """Resize an image to fit within the specified dimensions.

    :param image: the input image
    :param max_size: the maximum width and height as a tuple
    :return: the resized image, or the original image if it fits within the
        specified dimensions
    """
    width, height = image.size
    max_width, max_height = max_size

    if width > max_width or height > max_height:
        new_image = image.copy()
        new_image.thumbnail((max_width, max_height))
        return new_image

    return image
