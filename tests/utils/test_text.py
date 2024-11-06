import pytest

from openfoodfacts.utils.text import get_tag


@pytest.mark.parametrize(
    "value,output",
    [
        ("Reflets de France", "reflets-de-france"),
        ("écrasé", "ecrase"),
        ("œufs de plein air", "oeufs-de-plein-air"),
        ("dr.oetker", "dr-oetker"),
        ("mat & lou", "mat-lou"),
        ("monop'daily", "monop-daily"),
        ("épi d'or", "epi-d-or"),
        ("Health Star Rating 0.5", "health-star-rating-0-5"),
        ("C'est qui le Patron ?!", "c-est-qui-le-patron"),
        ("fr: Gésiers", "fr:gesiers"),
        ("ar: تفاح", "ar:تفاح"),
        ("تفاح", "تفاح"),
    ],
)
def test_get_tag(value: str, output: str):
    assert get_tag(value) == output
