import pytest
from openfoodfacts.facet_container import FacetContainer

def test_facet_container_initialization():
    """Test that the container initializes with correct defaults."""
    container = FacetContainer(facet_name="brands")
    assert container.facet_name == "brands"
    assert container.data == []
    assert container.page_size == 20
    assert container.current_page == 1

def test_pagination_logic():
    """Test that get_page returns the correct slice of data."""

    dummy_data = list(range(50))
    container = FacetContainer(facet_name="test", data=dummy_data, page_size=10)

    page_1 = container.get_page(1)
    assert len(page_1) == 10
    assert page_1[0] == 0
    assert page_1[-1] == 9

    page_2 = container.get_page(2)
    assert page_2[0] == 10
    assert page_2[-1] == 19

def test_pagination_out_of_bounds():
    
    dummy_data = [1, 2, 3]
    container = FacetContainer(facet_name="test", data=dummy_data, page_size=10)

    # Page 2 should be empty
    assert container.get_page(2) == []
    
    # Page 0 or negative should handle gracefully (empty or error depending on your logic)
    assert container.get_page(0) == []

def test_total_pages_calculation():
    """Test the total_pages property."""

    c1 = FacetContainer(data=list(range(50)), page_size=10)
    assert c1.total_pages == 5

    c2 = FacetContainer(data=list(range(51)), page_size=10)
    assert c2.total_pages == 6

    c3 = FacetContainer(data=[], page_size=10)
    assert c3.total_pages == 0