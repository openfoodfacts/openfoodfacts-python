
import pytest
from openfoodfacts.utils import clean_string

def test_clean_string():
    assert clean_string(" Hello ") == "hello"
    assert clean_string("WORLD") == "world"
    assert clean_string("") == ""
    assert clean_string(None) is None