import json
import re
import unittest

import pytest
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

    def test_get_product_missing(self):
        api = openfoodfacts.API(user_agent=TEST_USER_AGENT, version="v2")
        code = "1223435"
        response_data = {
            "status": 0,
            "status_verbose": "product not found",
        }
        with requests_mock.mock() as mock:
            mock.get(
                f"https://world.openfoodfacts.org/api/v2/product/{code}",
                text=json.dumps(response_data),
                status_code=404,
            )
            res = api.product.get(code)
            self.assertEqual(res, None)

    def test_get_product_with_fields(self):
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
            res = api.product.get(code, fields=["code"])
            self.assertEqual(res, response_data["product"])
            self.assertEqual(mock.last_request.qs["fields"], ["code"])

    def test_get_product_invalid_code(self):
        api = openfoodfacts.API(user_agent=TEST_USER_AGENT, version="v2")
        code = "84800002930392025252502520502"
        response_data = {
            "status": 0,
            "status_verbose": "no code or invalid code",
        }
        with requests_mock.mock() as mock:
            mock.get(
                f"https://world.openfoodfacts.org/api/v2/product/{code}",
                text=json.dumps(response_data),
                status_code=200,
            )
            res = api.product.get(code)
            self.assertEqual(res, None)

            with pytest.raises(
                ValueError,
                match="invalid barcode: 84800002930392025252502520502",
            ):
                api.product.get(code, raise_if_invalid=True)

    def test_text_search(self):
        api = openfoodfacts.API(user_agent=TEST_USER_AGENT, version="v2")
        with requests_mock.mock() as mock:
            response_data = {"products": ["kinder bueno"], "count": 1}
            mock.get(
                "https://world.openfoodfacts.org/cgi/search.pl?"
                + "search_terms=kinder+bueno&json=1&page="
                + "1&page_size=20",
                text=json.dumps(response_data),
            )
            res = api.product.text_search("kinder bueno")
            self.assertEqual(res["products"], ["kinder bueno"])
            response_data = {"products": ["banania", "banania big"], "count": 2}
            mock.get(
                "https://world.openfoodfacts.org/cgi/search.pl?"
                + "search_terms=banania&json=1&page="
                + "2&page_size=10&sort_by=unique_scans",
                text=json.dumps(response_data),
            )
            res = api.product.text_search(
                "banania", page=2, page_size=10, sort_by="unique_scans"
            )
            self.assertEqual(res["products"], ["banania", "banania big"])

    def test_parse_ingredients(self):
        api = openfoodfacts.API(user_agent=TEST_USER_AGENT, version="v2")
        ingredients_data = [
            {
                "ciqual_food_code": "18066",
                "ecobalyse_code": "tap-water",
                "id": "en:water",
                "is_in_taxonomy": 1,
                "percent_estimate": 75,
                "percent_max": 100,
                "percent_min": 50,
                "text": "eau",
                "vegan": "yes",
                "vegetarian": "yes",
            },
            {
                "ciqual_proxy_food_code": "31016",
                "ecobalyse_code": "sugar",
                "id": "en:sugar",
                "is_in_taxonomy": 1,
                "percent_estimate": 25,
                "percent_max": 50,
                "percent_min": 0,
                "text": "sucre",
                "vegan": "yes",
                "vegetarian": "yes",
            },
        ]
        with requests_mock.mock() as mock:
            response_data = {
                "product": {"ingredients": ingredients_data},
                "status": "success",
            }
            mock.patch(
                "https://world.openfoodfacts.org/api/v3/product/test",
                text=json.dumps(response_data),
            )
            res = api.product.parse_ingredients("eau, sucre", lang="fr")
            assert res == ingredients_data

    def test_parse_ingredients_fail(self):
        api = openfoodfacts.API(user_agent=TEST_USER_AGENT, version="v2")
        with requests_mock.mock() as mock:
            response_data = {
                "status": "fail",
            }
            mock.patch(
                "https://world.openfoodfacts.org/api/v3/product/test",
                text=json.dumps(response_data),
            )

            with pytest.raises(
                RuntimeError,
                match="Unable to parse ingredients: {'status': 'fail'}",
            ):
                api.product.parse_ingredients("eau, sucre", lang="fr")

    def test_parse_ingredients_fail_non_HTTP_200(self):
        api = openfoodfacts.API(user_agent=TEST_USER_AGENT, version="v2")
        with requests_mock.mock() as mock:
            mock.patch(
                "https://world.openfoodfacts.org/api/v3/product/test",
                status_code=400,
                text='{"error": "Bad Request"}',
            )

            with pytest.raises(
                RuntimeError,
                match=re.escape(
                    'Unable to parse ingredients (non-200 status code): 400, {"error": "Bad Request"}'
                ),
            ):
                api.product.parse_ingredients("eau, sucre", lang="fr")


if __name__ == "__main__":
    unittest.main()
