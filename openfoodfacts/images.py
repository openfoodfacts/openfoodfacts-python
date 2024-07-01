import logging
import re
from pathlib import Path
from typing import List, Optional, Tuple, Union
from urllib.parse import urlparse

import requests
from PIL import Image

from openfoodfacts.types import Environment, Flavor
from openfoodfacts.utils import URLBuilder, get_image_from_url

logger = logging.getLogger(__name__)


BARCODE_PATH_REGEX = re.compile(r"^(...)(...)(...)(.*)$")
# Base URL of the public Open Food Facts S3 bucket
AWS_S3_BASE_URL = "https://openfoodfacts-images.s3.eu-west-3.amazonaws.com/data"


def split_barcode(barcode: str) -> List[str]:
    """Split barcode in the same way as done by Product Opener to generate a
    product image folder.

    :param barcode: The barcode of the product. For the pro platform only,
        it must be prefixed with the org ID using the format
        `{ORG_ID}/{BARCODE}`
    :raises ValueError: raise a ValueError if `barcode` is invalid
    :return: a list containing the splitted barcode
    """
    org_id = None
    if "/" in barcode:
        # For the pro platform, `barcode` is expected to be in the format
        # `{ORG_ID}/{BARCODE}` (ex: `org-lea-nature/3307130803004`)
        org_id, barcode = barcode.split("/", maxsplit=1)

    if not barcode.isdigit():
        raise ValueError(f"unknown barcode format: {barcode}")

    match = BARCODE_PATH_REGEX.fullmatch(barcode)

    splits = [x for x in match.groups() if x] if match else [barcode]

    if org_id is not None:
        # For the pro platform only, images and OCRs belonging to an org
        # are stored in a folder named after the org for all its products, ex:
        # https://images.pro.openfoodfacts.org/images/products/org-lea-nature/330/713/080/3004/1.jpg
        splits.append(org_id)

    return splits


def _generate_file_path(code: str, image_id: str, suffix: str):
    splitted_barcode = split_barcode(code)
    return f"/{'/'.join(splitted_barcode)}/{image_id}{suffix}"


def generate_image_path(code: str, image_id: str) -> str:
    """Generate an image path.

    It's used to generate a unique identifier of an image for a product (and
    to generate an URL to fetch this image from the server).

    :param code: the product barcode
    :param image_id: the image ID (ex: `1`, `ingredients_fr.full`,...)
    :return: the full image path
    """
    return _generate_file_path(code, image_id, ".jpg")


def generate_json_ocr_path(code: str, image_id: str) -> str:
    """Generate a JSON OCR path.

    It's used to generate a unique identifier of an OCR results for a product
    (and to generate an URL to fetch this OCR JSON from the server).

    :param code: the product barcode
    :param image_id: the image ID (ex: `1`, `ingredients_fr.full`,...)
    :return: the full image path
    """
    return _generate_file_path(code, image_id, ".json")


def generate_json_ocr_url(
    code: str,
    image_id: str,
    flavor: Flavor = Flavor.off,
    environment: Environment = Environment.org,
) -> str:
    """Generate the OCR JSON URL for a specific product and
    image ID.

    :param code: the product barcode
    :param image_id: the image ID (ex: `1`, `2`,...)
    :param flavor: the project to use, defaults to Flavor.off
    :param environment: the environment (prod/staging), defaults to
        Environment.org
    :return: the generated JSON URL
    """
    return (
        URLBuilder.static(flavor, environment)
        + f"/images/products{generate_json_ocr_path(code, image_id)}"
    )


def generate_image_url(
    code: str,
    image_id: str,
    flavor: Flavor = Flavor.off,
    environment: Environment = Environment.org,
) -> str:
    """Generate the image URL for a specific product and
    image ID.

    :param code: the product barcode
    :param image_id: the image ID (ex: `1`, `ingredients_fr.full`,...)
    :param flavor: the project to use, defaults to Flavor.off
    :param environment: the environment (prod/staging), defaults to
        Environment.org
    :return: the generated image URL
    """
    return URLBuilder.image_url(
        flavor, environment, generate_image_path(code, image_id)
    )


def extract_barcode_from_url(url: str) -> Optional[str]:
    """Extract a product barcode from an image/OCR URL.

    :param url: the URL
    :return: the extracted barcode
    """
    url_path = urlparse(url).path
    return extract_barcode_from_path(url_path)


def extract_barcode_from_path(path: str) -> Optional[str]:
    barcode = ""

    for parent in Path(path).parents:
        if parent.name.isdigit():
            barcode = parent.name + barcode
        else:
            break

    return barcode or None


def extract_source_from_url(url: str) -> str:
    """Extract source image from an image or OCR URL.

    The source image is a unique identifier of the image or OCR,
    and is the full path of the image or OCR file on the server
    (ex: `/008/009/637/2472/1.jpg`).

    :param url: the URL
    :return: the source image
    """
    url_path = urlparse(url).path

    if url_path.startswith("/images/products"):
        url_path = url_path[len("/images/products") :]

    if url_path.endswith(".json"):
        url_path = str(Path(url_path).with_suffix(".jpg"))

    return url_path


def download_image(
    image: Union[str, Tuple[str, str]],
    use_cache: bool = True,
    error_raise: bool = True,
    session: Optional[requests.Session] = None,
    return_bytes: bool = False,
) -> Union[None, Image.Image, Tuple[Optional[Image.Image], bytes]]:
    """Download an Open Food Facts image.

    :param image: the image URL or a tuple containing the barcode and the
        image ID
    :param use_cache: whether to use the S3 dataset cache, defaults to True
    :param error_raise: whether to raise an error if the download fails,
        defaults to True
    :param session: the requests session to use, defaults to None
    :param return_bytes: if True, return the image bytes as well, defaults to
        False.
    :return: the loaded image or None if an error occured. If `return_bytes`
        is True, a tuple with the image and the image bytes is returned.

    >>> download_image("https://images.openfoodfacts.org/images/products/324/227/210/2359/4.jpg")
    <PIL.JpegImagePlugin.JpegImageFile image mode=RGB size=1244x1500>

    >>> download_image(("3242272102359", "4"))
    <PIL.JpegImagePlugin.JpegImageFile image mode=RGB size=1244x1500>
    """
    if isinstance(image, str):
        if use_cache:
            image_path = extract_source_from_url(image)
            image_url = f"{AWS_S3_BASE_URL}{image_path}"

            if requests.head(image_url).status_code != 200:
                logger.debug(f"Image not found in cache: {image_url}")
                image_url = image
        else:
            image_url = image

    if isinstance(image, tuple):
        if use_cache:
            image_path = generate_image_path(*image)
            image_url = f"{AWS_S3_BASE_URL}{image_path}"

            if requests.head(image_url).status_code != 200:
                logger.debug(f"Image not found in cache: {image_url}")
                image_url = generate_image_url(*image)
        else:
            image_url = generate_image_url(*image)

    logger.debug(f"Downloading image from {image_url}")
    return get_image_from_url(
        image_url,
        error_raise=error_raise,
        session=session,
        return_bytes=return_bytes,
    )
