import re
from pathlib import Path
from typing import List, Optional
from urllib.parse import urlparse

from openfoodfacts.types import Environment, Flavor
from openfoodfacts.utils import URLBuilder

BARCODE_PATH_REGEX = re.compile(r"^(...)(...)(...)(.*)$")


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
