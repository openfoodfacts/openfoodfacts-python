from typing import Optional

import pytest

from openfoodfacts.images import (
    extract_barcode_from_url,
    extract_source_from_url,
    generate_image_url,
    generate_json_ocr_url,
)
from openfoodfacts.types import Environment, Flavor


@pytest.mark.parametrize(
    "url,output",
    [
        (
            "https://world.openfoodfacts.org/images/products/541/012/672/6954/1.jpg",
            "5410126726954",
        ),
        (
            "https://world.openfoodfacts.org/images/products/541/012/672/6954/1.json",
            "5410126726954",
        ),
        ("https://world.openfoodfacts.org/images/products/invalid/1.json", None),
        ("https://world.openfoodfacts.org/images/products/252/535.bk/1.jpg", None),
    ],
)
def test_get_barcode_from_url(url: str, output: Optional[str]):
    assert extract_barcode_from_url(url) == output


@pytest.mark.parametrize(
    "url,output",
    [
        (
            "https://static.openfoodfacts.org/images/products/359/671/046/5248/3.jpg",
            "/359/671/046/5248/3.jpg",
        ),
        (
            "https://static.openfoodfacts.org/images/products/2520549/1.jpg",
            "/2520549/1.jpg",
        ),
        (
            "https://static.openfoodfacts.org/images/products/2520549/1.json",
            "/2520549/1.jpg",
        ),
    ],
)
def test_get_source_from_url(url: str, output: str):
    assert extract_source_from_url(url) == output


@pytest.mark.parametrize(
    "code,image_id,flavor,environment,expected",
    [
        (
            "5410126726954",
            "1",
            Flavor.off,
            Environment.org,
            "https://images.openfoodfacts.org/images/products/541/012/672/6954/1.jpg",
        ),
        (
            "990530101113758685",
            "2",
            Flavor.off,
            Environment.org,
            "https://images.openfoodfacts.org/images/products/990/530/101/113758685/2.jpg",
        ),
        (
            "6539",
            "1",
            Flavor.off,
            Environment.org,
            "https://images.openfoodfacts.org/images/products/000/000/000/6539/1.jpg",
        ),
        (
            "12458465",
            "2.400",
            Flavor.obf,
            Environment.net,
            "https://images.openbeautyfacts.net/images/products/000/001/245/8465/2.400.jpg",
        ),
        (
            "org-lea-nature/5410126726954",
            "1",
            Flavor.off_pro,
            Environment.org,
            "https://images.pro.openfoodfacts.org/images/products/org-lea-nature/541/012/672/6954/1.jpg",
        ),
    ],
)
def test_generate_image_url(code, image_id, flavor, environment, expected):
    assert generate_image_url(code, image_id, flavor, environment) == expected


@pytest.mark.parametrize(
    "code,image_id,flavor,environment,expected",
    [
        (
            "5410126726954",
            "1",
            Flavor.off,
            Environment.org,
            "https://images.openfoodfacts.org/images/products/541/012/672/6954/1.json",
        ),
        (
            "6539",
            "1",
            Flavor.off,
            Environment.org,
            "https://images.openfoodfacts.org/images/products/000/000/000/6539/1.json",
        ),
        (
            "org-lea-nature/5410126726954",
            "1",
            Flavor.off_pro,
            Environment.org,
            "https://images.pro.openfoodfacts.org/images/products/org-lea-nature/541/012/672/6954/1.json",
        ),
    ],
)
def test_generate_json_ocr_url(code, image_id, flavor, environment, expected):
    assert generate_json_ocr_url(code, image_id, flavor, environment) == expected


@pytest.mark.parametrize(
    "url,expected",
    [
        (
            "https://world.openfoodfacts.org/images/products/541/012/672/6954/1.jpg",
            "5410126726954",
        ),
        (
            "https://world.openbeautyfacts.net/images/products/000/000/001/6954/1.jpg",
            "00016954",
        ),
        (
            "https://world.openbeautyfacts.net/images/products/000/009/121/6954/1.jpg",
            "91216954",
        ),
        (
            "https://world.openbeautyfacts.net/images/products/000/019/121/6954/1.jpg",
            "0000191216954",
        ),
        (
            "https://world.openbeautyfacts.net/images/products/343/919/121/6954/1.jpg",
            "3439191216954",
        ),
        (
            "https://world.openbeautyfacts.net/images/products/343/919/121/6954862052/1.jpg",
            "3439191216954862052",
        ),
    ],
)
def test_extract_barcode_from_url(url, expected):
    assert extract_barcode_from_url(url) == expected
