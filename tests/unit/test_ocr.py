from typing import Optional, Tuple

import pytest

from openfoodfacts.ocr import OCRResult


@pytest.mark.parametrize(
    "ocr_url, bounding_box, expected_text",
    [
        (
            # It corresponds to this OCR crop:
            # https://robotoff.openfoodfacts.org/api/v1/images/crop?image_url=https://images.openfoodfacts.org/images/products/089/000/000/1202/1.jpg&y_min=0.08416666666666667&x_min=0.30077691453940064&y_max=0.09583333333333334&x_max=0.37735849056603776
            "https://raw.githubusercontent.com/openfoodfacts/test-data/main/openfoodfacts-python/tests/unit/0890000001202_1.json",
            [101, 271, 115, 340],
            "Materne",
        ),
        (
            # same, but the bounding box is distinct from the logo area
            "https://raw.githubusercontent.com/openfoodfacts/test-data/main/openfoodfacts-python/tests/unit/0890000001202_1.json",
            [120, 271, 134, 340],
            None,
        ),
        (
            # same, but the bounding box is distinct from the logo area
            "https://raw.githubusercontent.com/openfoodfacts/test-data/main/openfoodfacts-python/tests/unit/0890000001202_1.json",
            [120, 271, 134, 340],
            None,
        ),
        (
            # [0.2808293402194977,0.37121888995170593,0.35544055700302124,0.49409016966819763]
            # /540/091/030/1160/1.jpg
            "https://raw.githubusercontent.com/openfoodfacts/test-data/main/openfoodfacts-python/tests/unit/5400910301160_1.json",
            [337, 327, 427, 436],
            "NUTRIDIA",
        ),
    ],
)
def test_get_words_in_area(
    ocr_url: str, bounding_box: Tuple[int, int, int, int], expected_text: Optional[str]
):
    ocr_result = OCRResult.from_url(ocr_url)
    assert ocr_result is not None
    words = ocr_result.get_words_in_area(bounding_box)

    if expected_text is None:
        assert words == []
    else:
        assert words is not None
        assert len(words) == 1
        assert words[0].text.strip() == expected_text
