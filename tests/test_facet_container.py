import pytest
from openfoodfacts.facet_container import FacetContainer

class MockFacetResource:
    def get(self, facet_name, page, page_size, **kwargs):
        if page > 2:
            return {}
        return {
            "tags": [{"name": f"item_{page}_{i}"} for i in range(page_size)]
        }

def test_facet_container_iteration():
    """Test that the container yields items from multiple pages correctly."""
    mock_api = MockFacetResource()
    container = FacetContainer(mock_api, facet_name="brands", page_size=5)
    all_items = list(container)
    assert len(all_items) == 10
    assert all_items[0]['name'] == "item_1_0"
    assert all_items[5]['name'] == "item_2_0"

def test_empty_results():
    """Test behavior when the API returns nothing."""
    class EmptyMockAPI:
        def get(self, *args, **kwargs):
            return {} 
    container = FacetContainer(EmptyMockAPI(), "brands")
    assert list(container) == []