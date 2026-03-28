











from unittest.mock import patch, Mock
from openfoodfacts.api import FacetResource 

def test_get_categories_pagination():
    """
    Test that get_categories properly paginates the static taxonomy 
    without hitting the live API.
    """
    # 1. Create a mock object to represent the Taxonomy class
    mock_taxonomy_obj = Mock()
    
    # 2. Helper function to create mock nodes that possess a .to_dict() method
    def create_mock_node(category_id, name):
        node = Mock()
        node.to_dict.return_value = {"id": category_id, "name": name}
        return node

    # 3. Create our 5 mock nodes
    mock_nodes = [
        create_mock_node("en:category1", "Category 1"),
        create_mock_node("en:category2", "Category 2"),
        create_mock_node("en:category3", "Category 3"),
        create_mock_node("en:category4", "Category 4"),
        create_mock_node("en:category5", "Category 5"),
    ]

    # 4. Tell the taxonomy mock to return our mock nodes
    mock_taxonomy_obj.iter_nodes.return_value = mock_nodes

    # 5. Patch get_taxonomy to return our custom mock object
    with patch('openfoodfacts.api.get_taxonomy', return_value=mock_taxonomy_obj):
        
        fake_config = Mock()
        resource = FacetResource(api_config=fake_config)

        # Test Page 1 (Should return the first 2 items)
        page1 = resource.get_categories(page=1, page_size=2)
        assert len(page1) == 2, "Page 1 should return exactly 2 items"
        assert page1[0]["id"] == "en:category1"
        
        # Test Page 2 (Should return the next 2 items)
        page2 = resource.get_categories(page=2, page_size=2)
        assert len(page2) == 2, "Page 2 should return exactly 2 items"
        assert page2[0]["id"] == "en:category3"
        
        # Test Page 3 (Should return the remaining 1 item)
        page3 = resource.get_categories(page=3, page_size=2)
        assert len(page3) == 1, "Page 3 should return the 1 remaining item"

        # Ensure the items are actually different
        assert page1 != page2, "Page 1 and Page 2 should have different categories"
