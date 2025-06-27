import pytest

from openfoodfacts.utils.text import get_tag, replace_lang_prefix


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


@pytest.mark.parametrize(
    "tag,new_lang_prefix,output",
    [
        ("fr:gesiers", "en", "en:gesiers"),
        ("fr:gesiers", "fr", "fr:gesiers"),
        ("fr:gesiers", "ar", "ar:gesiers"),
        ("en:apple", "fr", "fr:apple"),
        ("xx:sashimi", "it", "it:sashimi"),
        ("xx:sashimi", "xx", "xx:sashimi"),
    ],
)
def test_replace_lang_prefix(tag, new_lang_prefix, output):
    assert replace_lang_prefix(tag, new_lang_prefix) == output


def test_replace_lang_prefix_invalid_new_lang_prefix():
    with pytest.raises(ValueError, match="new_lang_prefix 'a' must be a 2-letter code"):
        replace_lang_prefix("en:apples", "a")


def test_replace_lang_prefix_invalid_tag():
    with pytest.raises(
        ValueError, match="tag 'e:apples' has an invalid language prefix"
    ):
        replace_lang_prefix("e:apples", "fr")
