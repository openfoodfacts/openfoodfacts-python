import pytest

from openfoodfacts.types import Flavor


def test_from_product_type_food():
    assert Flavor.from_product_type("food") == Flavor.off


def test_from_product_type_beauty():
    assert Flavor.from_product_type("beauty") == Flavor.obf


def test_from_product_type_petfood():
    assert Flavor.from_product_type("petfood") == Flavor.opff


def test_from_product_type_product():
    assert Flavor.from_product_type("product") == Flavor.opf


def test_from_product_type_invalid():
    with pytest.raises(
        ValueError, match="no Flavor matched with product_type 'invalid'"
    ):
        Flavor.from_product_type("invalid")
