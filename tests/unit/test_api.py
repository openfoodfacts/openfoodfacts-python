import json
import re

import pytest
import requests_mock

import openfoodfacts

TEST_USER_AGENT = "test_off_python"


class TestProducts:
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
            assert res == response_data["product"]

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
            assert res is None

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
            assert res == response_data["product"]
            assert mock.last_request.qs["fields"] == ["code"]

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
            assert res is None

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
            assert res["products"] == ["kinder bueno"]
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
            assert res["products"] == ["banania", "banania big"]

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
                    "Unable to parse ingredients (non-200 status code): 400, "
                    '{"error": "Bad Request"}'
                ),
            ):
                api.product.parse_ingredients("eau, sucre", lang="fr")

    def test_upload_image_success(self):
        api = openfoodfacts.API(
            user_agent=TEST_USER_AGENT,
            version="v3",
            username="test",
            password="test",
        )
        code = "1223435"
        response_data = {
            "code": "1223435",
            "errors": [],
            "product": {
                "images": {
                    "uploaded": {
                        "1": {
                            "imgid": 1,
                            "sizes": {
                                "100": {"h": 100, "w": 62},
                                "400": {"h": 400, "w": 248},
                                "full": {"h": 400, "w": 248},
                            },
                            "uploaded_t": 1758793764,
                            "uploader": "test",
                        }
                    }
                }
            },
            "result": {
                "id": "image_uploaded",
                "lc_name": "Image uploaded",
                "name": "Image uploaded",
            },
            "status": "success",
            "warnings": [],
        }
        with requests_mock.mock() as mock:
            mock.post(
                f"https://world.openfoodfacts.org/api/v3/product/{code}/images",
                text=json.dumps(response_data),
                status_code=200,
            )
            res = api.product.upload_image(code, image_data_base64="dGVzdA==")
            assert res.status_code == 200
            assert mock.last_request.json() == {
                "image_data_base64": "dGVzdA==",
                "user_id": "test",
                "password": "test",
            }

    def test_upload_image_with_selected(self):
        api = openfoodfacts.API(
            user_agent=TEST_USER_AGENT, version="v3", username="test", password="test"
        )
        code = "1223435"
        response_data = {
            "code": "1223435",
            "errors": [],
            "product": {
                "images": {
                    "selected": {
                        "front": {
                            "en": {
                                "generation": {},
                                "imgid": 1,
                                "rev": 2,
                                "sizes": {
                                    "100": {"h": 100, "w": 62},
                                    "200": {"h": 200, "w": 124},
                                    "400": {"h": 400, "w": 248},
                                    "full": {"h": 400, "w": 248},
                                },
                            }
                        }
                    },
                    "uploaded": {
                        "1": {
                            "imgid": 1,
                            "sizes": {
                                "100": {"h": 100, "w": 62},
                                "400": {"h": 400, "w": 248},
                                "full": {"h": 400, "w": 248},
                            },
                            "uploaded_t": 1758793852,
                            "uploader": "test",
                        }
                    },
                }
            },
            "result": {
                "id": "image_uploaded",
                "lc_name": "Image uploaded",
                "name": "Image uploaded",
            },
            "status": "success",
            "warnings": [],
        }
        with requests_mock.mock() as mock:
            mock.post(
                f"https://world.openfoodfacts.org/api/v3/product/{code}/images",
                text=json.dumps(response_data),
                status_code=200,
            )
            res = api.product.upload_image(
                code, image_data_base64="dGVzdA==", selected={"front": {"en": {}}}
            )
            assert res.status_code == 200
            assert mock.last_request.json() == {
                "image_data_base64": "dGVzdA==",
                "user_id": "test",
                "password": "test",
                "selected": {"front": {"en": {}}},
            }

    def test_upload_image_no_auth(self):
        api = openfoodfacts.API(user_agent=TEST_USER_AGENT, version="v3")
        code = "1223435"
        with pytest.raises(
            ValueError,
            match="a password or a session cookie is required to upload an image",
        ):
            api.product.upload_image(code, image_data_base64="dGVzdA==")

    def test_upload_image_invalid_code(self):
        api = openfoodfacts.API(
            user_agent=TEST_USER_AGENT, version="v3", username="test", password="test"
        )
        code = "invalidcode"
        with pytest.raises(
            ValueError,
            match="code must be a numeric string",
        ):
            api.product.upload_image(code, image_data_base64="dGVzdA==")

    def test_upload_image_no_data(self):
        api = openfoodfacts.API(
            user_agent=TEST_USER_AGENT, version="v3", username="test", password="test"
        )
        code = "1223435"
        with pytest.raises(
            ValueError,
            match="one of image_path or image_data_base64 must be provided",
        ):
            api.product.upload_image(code)

    def test_upload_image_both_data(self):
        api = openfoodfacts.API(
            user_agent=TEST_USER_AGENT, version="v3", username="test", password="test"
        )
        code = "1223435"
        with pytest.raises(
            ValueError,
            match="only one of image_path or image_data_base64 must be provided",
        ):
            api.product.upload_image(
                code, image_path="path/to/image.jpg", image_data_base64="dGVzdA=="
            )

    def test_upload_image_invalid_selected(self):
        api = openfoodfacts.API(
            user_agent=TEST_USER_AGENT, version="v3", username="test", password="test"
        )
        code = "1223435"
        with pytest.raises(
            ValueError,
            match=re.escape(
                "invalid image field name in selected: wrong (must be one of front, "
                "ingredients, nutrition, packaging)"
            ),
        ):
            api.product.upload_image(
                code, image_data_base64="dGVzdA==", selected={"wrong": {}}
            )

    def test_upload_image_with_path(self, tmp_path):
        api = openfoodfacts.API(
            user_agent=TEST_USER_AGENT, version="v3", username="test", password="test"
        )
        code = "1223435"
        response_data = {
            "code": "1223435",
            "errors": [],
            "product": {
                "images": {
                    "uploaded": {
                        "1": {
                            "imgid": 1,
                            "sizes": {
                                "100": {"h": 100, "w": 62},
                                "400": {"h": 400, "w": 248},
                                "full": {"h": 400, "w": 248},
                            },
                            "uploaded_t": 1758793764,
                            "uploader": "test",
                        }
                    }
                }
            },
            "result": {
                "id": "image_uploaded",
                "lc_name": "Image uploaded",
                "name": "Image uploaded",
            },
            "status": "success",
            "warnings": [],
        }
        image_path = tmp_path / "test_image.jpg"
        image_path.write_bytes(b"test")
        with requests_mock.mock() as mock:
            mock.post(
                f"https://world.openfoodfacts.org/api/v3/product/{code}/images",
                text=json.dumps(response_data),
                status_code=200,
            )
            res = api.product.upload_image(code, image_path=image_path)
            assert res.status_code == 200
            assert mock.last_request.json() == {
                "image_data_base64": "dGVzdA==",
                "user_id": "test",
                "password": "test",
            }


class TestSendRequest:
    """Unit tests for the api._send_request function."""

    api_config = openfoodfacts.API(user_agent=TEST_USER_AGENT, version="v2").api_config

    def test_invalid_method(self):
        method = "invalid"
        with pytest.raises(NotImplementedError) as excinfo:
            openfoodfacts.api._send_request(
                "https://example.com/",
                api_config=self.api_config,
                method=method,
            )
        assert method in str(excinfo.value)

    def test_get_404_returns_none(self):
        method = "get"
        url = "https://world.openfoodfacts.org/api/v2/product/1223435"
        response_data = {
            "status": 0,
            "status_verbose": "product not found",
        }
        with requests_mock.mock() as mock:
            mock.get(
                url,
                text=json.dumps(response_data),
                status_code=404,
            )
            res = openfoodfacts.api._send_request(
                url,
                api_config=self.api_config,
                method=method,
                return_none_on_404=True,
            )
            assert res is None


class TestProductSearch:
    def test_product_search_basic(self):
        """search() builds correct URL with query param"""
        api = openfoodfacts.API(user_agent=TEST_USER_AGENT)
        response_data = {"hits": [], "count": 0}
        with requests_mock.mock() as mock:
            mock.get(
                "https://search.openfoodfacts.org/search?q=chocolate&page=1&page_size=24",
                json=response_data,
            )
            result = api.product.search("chocolate")
            assert result == response_data

    def test_product_search_with_pagination(self):
        """search() passes page and page_size params"""
        api = openfoodfacts.API(user_agent=TEST_USER_AGENT)
        response_data = {"hits": [], "count": 0}
        with requests_mock.mock() as mock:
            mock.get(
                "https://search.openfoodfacts.org/search?q=chocolate&page=2&page_size=10",
                json=response_data,
            )
            result = api.product.search("chocolate", page=2, page_size=10)
            assert result == response_data

    def test_product_search_with_sort_by(self):
        """search() passes sort_by param when provided"""
        api = openfoodfacts.API(user_agent=TEST_USER_AGENT)
        response_data = {"hits": [], "count": 0}
        with requests_mock.mock() as mock:
            mock.get(
                "https://search.openfoodfacts.org/search?q=chocolate&page=1&page_size=24&sort_by=unique_scans",
                json=response_data,
            )
            result = api.product.search("chocolate", sort_by="unique_scans")
            assert result == response_data

    def test_product_search_net_environment(self):
        """search() uses .net domain in net environment"""
        api = openfoodfacts.API(user_agent=TEST_USER_AGENT, environment="net")
        response_data = {"hits": [], "count": 0}
        with requests_mock.mock() as mock:
            mock.get(
                "https://search.openfoodfacts.net/search?q=chocolate&page=1&page_size=24",
                json=response_data,
            )
            result = api.product.search("chocolate")
            assert result == response_data


class TestNutriPatrol:
    def test_get_flag(self):
        api = openfoodfacts.API(
            user_agent=TEST_USER_AGENT, session_cookie="test_session"
        )
        flag_id = 123
        response_data = {"id": flag_id, "status": "open"}
        with requests_mock.mock() as mock:
            mock.get(
                f"https://nutripatrol.openfoodfacts.org/api/v1/flags/{flag_id}",
                json=response_data,
            )
            result = api.nutripatrol.get_flag(flag_id)
            assert result == response_data

    def test_get_flags(self):
        api = openfoodfacts.API(
            user_agent=TEST_USER_AGENT, session_cookie="test_session"
        )
        response_data = {"flags": []}
        with requests_mock.mock() as mock:
            mock.get(
                "https://nutripatrol.openfoodfacts.org/api/v1/flags",
                json=response_data,
            )
            result = api.nutripatrol.get_flags()
            assert result == response_data

    def test_create_flag(self):
        api = openfoodfacts.API(
            user_agent=TEST_USER_AGENT, session_cookie="test_session"
        )
        flag_data = {"barcode": "12345678", "reason": "wrong_category"}
        response_data = {"id": 1, **flag_data}
        with requests_mock.mock() as mock:
            mock.post(
                "https://nutripatrol.openfoodfacts.org/api/v1/flags",
                json=response_data,
            )
            result = api.nutripatrol.create_flag(flag_data)
            assert result == response_data
            assert mock.last_request.json() == flag_data

    def test_get_flags_by_ticket_batch(self):
        api = openfoodfacts.API(
            user_agent=TEST_USER_AGENT, session_cookie="test_session"
        )
        ticket_ids = [1, 2, 3]
        response_data = {"flags": []}
        with requests_mock.mock() as mock:
            mock.post(
                "https://nutripatrol.openfoodfacts.org/api/v1/flags/batch",
                json=response_data,
            )
            result = api.nutripatrol.get_flags_by_ticket_batch(ticket_ids)
            assert result == response_data
            assert mock.last_request.json() == {"ticket_ids": ticket_ids}

    def test_get_ticket(self):
        api = openfoodfacts.API(
            user_agent=TEST_USER_AGENT, session_cookie="test_session"
        )
        ticket_id = 456
        response_data = {"id": ticket_id}
        with requests_mock.mock() as mock:
            mock.get(
                f"https://nutripatrol.openfoodfacts.org/api/v1/tickets/{ticket_id}",
                json=response_data,
            )
            result = api.nutripatrol.get_ticket(ticket_id)
            assert result == response_data

    def test_get_tickets(self):
        api = openfoodfacts.API(
            user_agent=TEST_USER_AGENT, session_cookie="test_session"
        )
        response_data = {"tickets": []}
        with requests_mock.mock() as mock:
            mock.get(
                "https://nutripatrol.openfoodfacts.org/api/v1/tickets?page=1&page_size=10",
                json=response_data,
            )
            result = api.nutripatrol.get_tickets()
            assert result == response_data

    def test_get_tickets_with_filters(self):
        api = openfoodfacts.API(
            user_agent=TEST_USER_AGENT, session_cookie="test_session"
        )
        response_data = {"tickets": []}
        with requests_mock.mock() as mock:
            mock.get(
                "https://nutripatrol.openfoodfacts.org/api/v1/tickets?page=2&page_size=20&barcode=123&status=open",
                json=response_data,
            )
            result = api.nutripatrol.get_tickets(
                barcode="123", status="open", page=2, page_size=20
            )
            assert result == response_data

    def test_update_ticket_status(self):
        api = openfoodfacts.API(
            user_agent=TEST_USER_AGENT, session_cookie="test_session"
        )
        ticket_id = 456
        status = "closed"
        response_data = {"id": ticket_id, "status": status}
        with requests_mock.mock() as mock:
            mock.put(
                f"https://nutripatrol.openfoodfacts.org/api/v1/tickets/{ticket_id}/status?status={status}",
                json=response_data,
            )
            result = api.nutripatrol.update_ticket_status(ticket_id, status)
            assert result == response_data

    def test_get_stats(self):
        api = openfoodfacts.API(
            user_agent=TEST_USER_AGENT, session_cookie="test_session"
        )
        response_data = {"stats": {}}
        with requests_mock.mock() as mock:
            mock.get(
                "https://nutripatrol.openfoodfacts.org/api/v1/stats?n_days=31",
                json=response_data,
            )
            result = api.nutripatrol.get_stats()
            assert result == response_data

    def test_status(self):
        api = openfoodfacts.API(
            user_agent=TEST_USER_AGENT, session_cookie="test_session"
        )
        response_data = {"status": "ok"}
        with requests_mock.mock() as mock:
            mock.get(
                "https://nutripatrol.openfoodfacts.org/api/v1/status",
                json=response_data,
            )
            result = api.nutripatrol.status()
            assert result == response_data

    def test_nutripatrol_methods_require_cookie_auth(self):
        api = openfoodfacts.API(user_agent=TEST_USER_AGENT)

        with pytest.raises(ValueError, match="session_cookie must be set"):
            api.nutripatrol.get_flag(123)

        with pytest.raises(ValueError, match="session_cookie must be set"):
            api.nutripatrol.get_flags()

        with pytest.raises(ValueError, match="session_cookie must be set"):
            api.nutripatrol.create_flag({"barcode": "123"})

        with pytest.raises(ValueError, match="session_cookie must be set"):
            api.nutripatrol.get_flags_by_ticket_batch([1, 2, 3])

        with pytest.raises(ValueError, match="session_cookie must be set"):
            api.nutripatrol.get_ticket(456)

        with pytest.raises(ValueError, match="session_cookie must be set"):
            api.nutripatrol.get_tickets()

        with pytest.raises(ValueError, match="session_cookie must be set"):
            api.nutripatrol.update_ticket_status(456, "closed")

        with pytest.raises(ValueError, match="session_cookie must be set"):
            api.nutripatrol.get_stats()

    def test_nutripatrol_status_works_without_auth(self):
        api = openfoodfacts.API(user_agent=TEST_USER_AGENT)
        response_data = {"status": "ok"}
        with requests_mock.mock() as mock:
            mock.get(
                "https://nutripatrol.openfoodfacts.org/api/v1/status",
                json=response_data,
            )
            result = api.nutripatrol.status()
            assert result == response_data

