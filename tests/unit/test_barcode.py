import pytest

from openfoodfacts.barcode import (
    calculate_check_digit,
    has_valid_check_digit,
    normalize_barcode,
)


def test_normalize_barcode_remove_leading_zeros():
    assert normalize_barcode("00012345") == "00012345"
    assert normalize_barcode("00000001") == "00000001"


def test_normalize_barcode_pad_to_8_digits():
    assert normalize_barcode("123") == "00000123"
    assert normalize_barcode("1") == "00000001"


def test_normalize_barcode_pad_to_13_digits():
    assert normalize_barcode("123456789") == "0000123456789"
    assert normalize_barcode("123456789012") == "0123456789012"


def test_normalize_barcode_no_change_needed():
    assert normalize_barcode("12345678") == "12345678"
    assert normalize_barcode("1234567890123") == "1234567890123"


@pytest.mark.parametrize(
    "gtin,expected",
    [
        ("3017620422003", "3"),
        ("8901234567890", "0"),
        ("101011", "1"),
        ("000101011", "1"),
        ("0000000101011", "1"),
        ("5678989012342", "2"),
        ("829573994253", "3"),
        ("59366631014", "4"),
        ("150599289765", "5"),
        ("9012345678906", "6"),
        ("360131017", "7"),
        ("1234567890128", "8"),
        ("10061282", "2"),
    ],
)
def test_calculate_check_digit(gtin, expected):
    assert calculate_check_digit(gtin) == expected


@pytest.mark.parametrize(
    "gtin,expected",
    [
        ("3017620422003", True),
        ("0204341706595", True),
        ("5707196311419", True),
        ("5701018060158", True),
        ("5016451522591", True),
        ("5741000224168", True),
        ("5741000224168", True),
        ("0256844308646", True),
        ("0083012245843", True),
        ("5741000224161", False),
        # EAN8
        ("10061282", True),
        ("10061283", False),
        ("0000010061282", True),
        ("29428984", True),
    ],
)
def test_has_valid_check_digit(gtin, expected):
    assert has_valid_check_digit(gtin) is expected
