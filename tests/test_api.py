import json
import unittest

import requests_mock

import openfoodfacts

TEST_USER_AGENT = "test_off_python"


class TestProducts(unittest.TestCase):
    def test_get_product(self):
        api = openfoodfacts.API(user_agent=TEST_USER_AGENT, version="v2")
        code = "1223435"
        response_data = {
            "product": {"code": "1223435"},
            "status": 1,
            "status_verbose": "product found",
        }
        with requests_mock.mock() as mock:
            mock.get(
                f"https://world.openfoodfacts.org/api/v2/product/{code}",
                text=json.dumps(response_data),
            )
            res = api.product.get(code)
            self.assertEqual(res, response_data["product"])

    def test_text_search(self):
        api = openfoodfacts.API(user_agent=TEST_USER_AGENT, version="v2")
        with requests_mock.mock() as mock:
            response_data = {"products": ["kinder bueno"], "count": 1}
            mock.get(
                "https://world.openfoodfacts.org/api/v2/search?"
                + "search_terms=kinder+bueno&json=1&page="
                + "1&page_size=20",
                text=json.dumps(response_data),
            )
            res = api.product.text_search("kinder bueno")
            self.assertEqual(res["products"], ["kinder bueno"])
            response_data = {"products": ["banania", "banania big"], "count": 2}
            mock.get(
                "https://world.openfoodfacts.org/api/v2/search?"
                + "search_terms=banania&json=1&page="
                + "2&page_size=10&sort_by=unique_scans",
                text=json.dumps(response_data),
            )
            res = api.product.text_search(
                "banania", page=2, page_size=10, sort_by="unique_scans"
            )
            self.assertEqual(res["products"], ["banania", "banania big"])


if __name__ == "__main__":
    unittest.main()
