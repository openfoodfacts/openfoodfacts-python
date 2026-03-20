import pytest
import time
from unittest.mock import patch
from openfoodfacts.facet_container import FacetContainer

class MockFacetResource:
    def get(self, facet_name, page, page_size, **kwargs):
        if page == 1:
            return {
                "tags":[{"id": "brand:1", "name": "Coca-Cola"}],
                "products": [{"id": "prod:1", "name": "Diet Coke"}]
            }
        return {} 

class ErrorMockAPI:
    def get(self, *args, **kwargs):
        raise ConnectionError("Simulated Network Timeout")

def test_facet_iteration_default_tags():
    mock_api = MockFacetResource()
    container = FacetContainer(mock_api, facet_name="brand", page_size=10)
    results = list(container)
    assert len(results) == 1
    assert results[0]['name'] == "Coca-Cola"

def test_facet_iteration_dynamic_key():
    mock_api = MockFacetResource()
    container = FacetContainer(mock_api, facet_name="brand", page_size=10, data_key="products")
    results = list(container)
    assert len(results) == 1
    assert results[0]['name'] == "Diet Coke"

def test_empty_results():
    class EmptyAPI:
        def get(self, *args, **kwargs):
            return {} 
            
    container = FacetContainer(EmptyAPI(), "brand")
    assert list(container) == []

def test_network_failure_handling():
    mock_api = ErrorMockAPI()
    container = FacetContainer(mock_api, "brand")
    with patch("time.sleep", return_value=None):
        with pytest.raises(ConnectionError):
            list(container)