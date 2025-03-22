import unittest
from unittest import mock

from openfoodfacts import API
from openfoodfacts.types import APIConfig, Flavor, Country, APIVersion, Environment


class TestSearchALicious(unittest.TestCase):
    def setUp(self):
        self.api = API(
            user_agent="test-user-agent",
            flavor=Flavor.off,
            country=Country.world,
            version=APIVersion.v2,
            environment=Environment.org,
        )

    @mock.patch('openfoodfacts.search_a_licious.requests.post')
    def test_search(self, mock_post):
        # Mock the response
        mock_response = mock.Mock()
        mock_response.json.return_value = {
            "is_success": True, 
            "count": 100, 
            "items": [{"code": "1234", "product_name": "Test Product"}]
        }
        mock_response.raise_for_status.return_value = None
        mock_post.return_value = mock_response

        # Call the search method
        results = self.api.search_a_licious.search(query="test")
        
        # Check if the POST request was made with the expected parameters
        mock_post.assert_called_once()
        args, kwargs = mock_post.call_args
        self.assertEqual(kwargs['json']['query'], "test")
        
        # Check if the results are as expected
        self.assertEqual(results['count'], 100)
        self.assertEqual(len(results['items']), 1)

    @mock.patch('openfoodfacts.search_a_licious.requests.get')
    def test_autocomplete(self, mock_get):
        # Mock the response
        mock_response = mock.Mock()
        mock_response.json.return_value = {
            "is_success": True,
            "suggestions": [{"text": "chocolate"}, {"text": "chocolate chips"}]
        }
        mock_response.raise_for_status.return_value = None
        mock_get.return_value = mock_response

        # Call the autocomplete method
        results = self.api.search_a_licious.autocomplete(q="choc", taxonomy_names="ingredients")
        
        # Check if the GET request was made with the expected parameters
        mock_get.assert_called_once()
        args, kwargs = mock_get.call_args
        self.assertEqual(kwargs['params']['q'], "choc")
        
        # Check if the results are as expected
        self.assertEqual(len(results['suggestions']), 2)
        self.assertEqual(results['suggestions'][0]['text'], "chocolate")

if __name__ == '__main__':
    unittest.main()