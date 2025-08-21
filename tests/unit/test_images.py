from typing import Optional

import pytest

from openfoodfacts.images import (
    convert_to_legacy_schema,
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
        # Test that barcode normalization (stripping leading zeros) works
        # correctly
        (
            "0005410126726954",
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


IMAGES_WITH_LEGACY_SCHEMA = {
    "1": {
        "sizes": {
            "100": {"h": 100, "w": 56},
            "400": {"h": 400, "w": 225},
            "full": {"h": 3555, "w": 2000},
        },
        "uploaded_t": "1490702616",
        "uploader": "user1",
    },
    "2": {
        "sizes": {
            "100": {"h": 100, "w": 56},
            "400": {"h": 400, "w": 225},
            "full": {"h": 3555, "w": 2000},
        },
        "uploaded_t": "1490702690",
        "uploader": "user2",
    },
    "3": {
        "sizes": {
            "100": {"h": 100, "w": 56},
            "400": {"h": 400, "w": 225},
            "full": {"h": 3555, "w": 2000},
        },
        "uploaded_t": "1490702705",
        "uploader": "user2",
    },
    "front_fr": {
        "angle": None,
        "geometry": "0x0-0-0",
        "imgid": "3",
        "normalize": "0",
        "rev": "27",
        "sizes": {
            "100": {"h": 100, "w": 75},
            "200": {"h": 200, "w": 150},
            "400": {"h": 400, "w": 300},
            "full": {"h": 1200, "w": 901},
        },
        "white_magic": "0",
        "x1": None,
        "x2": None,
        "y1": None,
        "y2": None,
    },
    "ingredients_fr": {
        "angle": None,
        "geometry": "0x0-0-0",
        "imgid": "1",
        "normalize": "0",
        "ocr": 1,
        "orientation": "0",
        "rev": "29",
        "sizes": {
            "100": {"h": 40, "w": 100},
            "200": {"h": 81, "w": 200},
            "400": {"h": 162, "w": 400},
            "full": {"h": 1200, "w": 2972},
        },
        "white_magic": "0",
        "x1": None,
        "x2": None,
        "y1": None,
        "y2": None,
    },
    "nutrition_fr": {
        "angle": None,
        "geometry": "0x0-0-0",
        "imgid": "2",
        "normalize": "0",
        "ocr": 1,
        "orientation": "0",
        "rev": "18",
        "sizes": {
            "100": {"h": 53, "w": 100},
            "200": {"h": 107, "w": 200},
            "400": {"h": 213, "w": 400},
            "full": {"h": 1093, "w": 2050},
        },
        "white_magic": "0",
        "x1": None,
        "x2": None,
        "y1": None,
        "y2": None,
    },
}


IMAGES_WITH_NEW_SCHEMA = {
    "uploaded": {
        "1": {
            "sizes": {
                "100": {
                    "h": 100,
                    "w": 56,
                    "url": "https://images.openfoodfacts.org/images/products/326/385/950/6216/1.100.jpg",
                },
                "400": {
                    "h": 400,
                    "w": 225,
                    "url": "https://images.openfoodfacts.org/images/products/326/385/950/6216/1.400.jpg",
                },
                "full": {
                    "h": 3555,
                    "w": 2000,
                    "url": "https://images.openfoodfacts.org/images/products/326/385/950/6216/1.jpg",
                },
            },
            "uploaded_t": "1490702616",
            "uploader": "user1",
        },
        "2": {
            "sizes": {
                "100": {
                    "h": 100,
                    "w": 56,
                    "url": "https://images.openfoodfacts.org/images/products/326/385/950/6216/2.100.jpg",
                },
                "400": {
                    "h": 400,
                    "w": 225,
                    "url": "https://images.openfoodfacts.org/images/products/326/385/950/6216/2.400.jpg",
                },
                "full": {
                    "h": 3555,
                    "w": 2000,
                    "url": "https://images.openfoodfacts.org/images/products/326/385/950/6216/2.jpg",
                },
            },
            "uploaded_t": "1490702690",
            "uploader": "user2",
        },
        "3": {
            "sizes": {
                "100": {
                    "h": 100,
                    "w": 56,
                    "url": "https://images.openfoodfacts.org/images/products/326/385/950/6216/3.100.jpg",
                },
                "400": {
                    "h": 400,
                    "w": 225,
                    "url": "https://images.openfoodfacts.org/images/products/326/385/950/6216/3.400.jpg",
                },
                "full": {
                    "h": 3555,
                    "w": 2000,
                    "url": "https://images.openfoodfacts.org/images/products/326/385/950/6216/3.jpg",
                },
            },
            "uploaded_t": "1490702705",
            "uploader": "user2",
        },
    },
    "selected": {
        "front": {
            "fr": {
                "imgid": "3",
                "rev": "27",
                "sizes": {
                    "100": {
                        "h": 100,
                        "w": 75,
                        "url": "https://images.openfoodfacts.org/images/products/326/385/950/6216/front_fr.27.100.jpg",
                    },
                    "200": {
                        "h": 200,
                        "w": 150,
                        "url": "https://images.openfoodfacts.org/images/products/326/385/950/6216/front_fr.27.200.jpg",
                    },
                    "400": {
                        "h": 400,
                        "w": 300,
                        "url": "https://images.openfoodfacts.org/images/products/326/385/950/6216/front_fr.27.400.jpg",
                    },
                    "full": {
                        "h": 1200,
                        "w": 901,
                        "url": "https://images.openfoodfacts.org/images/products/326/385/950/6216/front_fr.27.full.jpg",
                    },
                },
                "generation": {
                    "white_magic": "0",
                    "x1": None,
                    "x2": None,
                    "y1": None,
                    "y2": None,
                    "normalize": "0",
                    "angle": None,
                    "geometry": "0x0-0-0",
                },
            },
        },
        "nutrition": {
            "fr": {
                "imgid": "2",
                "rev": "18",
                "sizes": {
                    "100": {
                        "h": 53,
                        "w": 100,
                        "url": "https://images.openfoodfacts.org/images/products/326/385/950/6216/nutrition_fr.18.100.jpg",
                    },
                    "200": {
                        "h": 107,
                        "w": 200,
                        "url": "https://images.openfoodfacts.org/images/products/326/385/950/6216/nutrition_fr.18.200.jpg",
                    },
                    "400": {
                        "h": 213,
                        "w": 400,
                        "url": "https://images.openfoodfacts.org/images/products/326/385/950/6216/nutrition_fr.18.400.jpg",
                    },
                    "full": {
                        "h": 1093,
                        "w": 2050,
                        "url": "https://images.openfoodfacts.org/images/products/326/385/950/6216/nutrition_fr.18.full.jpg",
                    },
                },
                "generation": {
                    "white_magic": "0",
                    "x1": None,
                    "x2": None,
                    "y1": None,
                    "y2": None,
                    "normalize": "0",
                    "ocr": 1,
                    "orientation": "0",
                    "angle": None,
                    "geometry": "0x0-0-0",
                },
            },
        },
        "ingredients": {
            "fr": {
                "imgid": "1",
                "rev": "29",
                "sizes": {
                    "100": {
                        "h": 40,
                        "w": 100,
                        "url": "https://images.openfoodfacts.org/images/products/326/385/950/6216/ingredients_fr.29.100.jpg",
                    },
                    "200": {
                        "h": 81,
                        "w": 200,
                        "url": "https://images.openfoodfacts.org/images/products/326/385/950/6216/ingredients_fr.29.200.jpg",
                    },
                    "400": {
                        "h": 162,
                        "w": 400,
                        "url": "https://images.openfoodfacts.org/images/products/326/385/950/6216/ingredients_fr.29.400.jpg",
                    },
                    "full": {
                        "h": 1200,
                        "w": 2972,
                        "url": "https://images.openfoodfacts.org/images/products/326/385/950/6216/ingredients_fr.29.full.jpg",
                    },
                },
                "generation": {
                    "white_magic": "0",
                    "x1": None,
                    "x2": None,
                    "y1": None,
                    "y2": None,
                    "normalize": "0",
                    "ocr": 1,
                    "orientation": "0",
                    "angle": None,
                    "geometry": "0x0-0-0",
                },
            }
        },
    },
}


@pytest.mark.parametrize(
    "images,expected_result",
    [
        ({}, {}),
        (IMAGES_WITH_LEGACY_SCHEMA, IMAGES_WITH_LEGACY_SCHEMA),
        (IMAGES_WITH_NEW_SCHEMA, IMAGES_WITH_LEGACY_SCHEMA),
        # No `generation` data
        (
            {
                "uploaded": {
                    "1": {
                        "sizes": {
                            "100": {
                                "h": 100,
                                "w": 56,
                                "url": "https://images.openfoodfacts.org/images/products/326/385/950/6216/1.100.jpg",
                            },
                            "400": {
                                "h": 400,
                                "w": 225,
                                "url": "https://images.openfoodfacts.org/images/products/326/385/950/6216/1.400.jpg",
                            },
                            "full": {
                                "h": 3555,
                                "w": 2000,
                                "url": "https://images.openfoodfacts.org/images/products/326/385/950/6216/1.jpg",
                            },
                        },
                        "uploaded_t": "1490702616",
                        "uploader": "user1",
                    },
                },
                "selected": {
                    "front": {
                        "fr": {
                            "imgid": "3",
                            "rev": "27",
                            "sizes": {
                                "100": {
                                    "h": 100,
                                    "w": 75,
                                    "url": "https://images.openfoodfacts.org/images/products/326/385/950/6216/front_fr.27.100.jpg",
                                },
                                "200": {
                                    "h": 200,
                                    "w": 150,
                                    "url": "https://images.openfoodfacts.org/images/products/326/385/950/6216/front_fr.27.200.jpg",
                                },
                                "400": {
                                    "h": 400,
                                    "w": 300,
                                    "url": "https://images.openfoodfacts.org/images/products/326/385/950/6216/front_fr.27.400.jpg",
                                },
                                "full": {
                                    "h": 1200,
                                    "w": 901,
                                    "url": "https://images.openfoodfacts.org/images/products/326/385/950/6216/front_fr.27.full.jpg",
                                },
                            },
                        },
                    }
                },
            },
            {
                "1": {
                    "sizes": {
                        "100": {"h": 100, "w": 56},
                        "400": {"h": 400, "w": 225},
                        "full": {"h": 3555, "w": 2000},
                    },
                    "uploaded_t": "1490702616",
                    "uploader": "user1",
                },
                "front_fr": {
                    "imgid": "3",
                    "rev": "27",
                    "sizes": {
                        "100": {"h": 100, "w": 75},
                        "200": {"h": 200, "w": 150},
                        "400": {"h": 400, "w": 300},
                        "full": {"h": 1200, "w": 901},
                    },
                },
            },
        ),
        # No `selected` data
        (
            {
                "uploaded": {
                    "1": {
                        "sizes": {
                            "100": {
                                "h": 100,
                                "w": 56,
                                "url": "https://images.openfoodfacts.org/images/products/326/385/950/6216/1.100.jpg",
                            },
                            "400": {
                                "h": 400,
                                "w": 225,
                                "url": "https://images.openfoodfacts.org/images/products/326/385/950/6216/1.400.jpg",
                            },
                            "full": {
                                "h": 3555,
                                "w": 2000,
                                "url": "https://images.openfoodfacts.org/images/products/326/385/950/6216/1.jpg",
                            },
                        },
                        "uploaded_t": "1490702616",
                        "uploader": "user1",
                    },
                },
            },
            {
                "1": {
                    "sizes": {
                        "100": {"h": 100, "w": 56},
                        "400": {"h": 400, "w": 225},
                        "full": {"h": 3555, "w": 2000},
                    },
                    "uploaded_t": "1490702616",
                    "uploader": "user1",
                },
            },
        ),
    ],
)
def test_convert_to_legacy_schema(images, expected_result):
    assert convert_to_legacy_schema(images) == expected_result
