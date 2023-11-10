from typing import Any, Dict, List, Optional, Tuple, Union

import requests

from .types import APIConfig, APIVersion, Country, Environment, Facet, Flavor, JSONType
from .utils import URLBuilder, http_session


def get_http_auth(environment: Environment) -> Optional[Tuple[str, str]]:
    return ("off", "off") if environment is Environment.net else None


def send_get_request(
    url: str, api_config: APIConfig, params: Optional[Dict[str, Any]] = None
) -> dict:
    r = http_session.get(
        url,
        params=params,
        timeout=api_config.timeout,
        auth=get_http_auth(api_config.environment),
    )
    r.raise_for_status()
    return r.json()


def send_for_urlencoded_post_request(
    url: str, body: Dict[str, Any], api_config: APIConfig
) -> requests.Response:
    if api_config.username and api_config.password:
        body["user_id"] = api_config.username
        body["password"] = api_config.password
    r = http_session.post(
        url,
        data=body,
        timeout=api_config.timeout,
        auth=get_http_auth(api_config.environment),
    )
    r.raise_for_status()
    return r


class FacetResource:
    def __init__(self, api_config: APIConfig):
        self.api_config = api_config
        self.base_url = URLBuilder.country(
            self.api_config.flavor,
            environment=api_config.environment,
            country_code=self.api_config.country.name,
        )

    def get(self, facet: Union[Facet, str]):
        if facet not in list(Facet):
            raise ValueError("unknown Facet: %s", facet)
        return send_get_request(
            url=f"{self.base_url}/{facet}",
            params={"json": "1"},
            api_config=self.api_config,
        )


class ProductResource:
    def __init__(self, api_config: APIConfig):
        self.api_config = api_config
        self.base_url = URLBuilder.country(
            self.api_config.flavor,
            environment=api_config.environment,
            country_code=self.api_config.country.name,
        )

    def get(self, code: str, fields: Optional[List[str]] = None) -> Optional[dict]:
        """Return a product.

        :param code: barcode of the product
        :param fields: a list of fields to return. If None, all fields are
            returned.
        :return: the API response
        """
        fields = fields or []
        url = f"{self.base_url}/api/{self.api_config.version}/product/{code}"

        if fields:
            # requests escape comma in URLs, as expected, but openfoodfacts
            # server does not recognize escaped commas.
            # See
            # https://github.com/openfoodfacts/openfoodfacts-server/issues/1607
            url += "?fields={}".format(",".join(fields))

        return send_get_request(url=url, api_config=self.api_config)

    def text_search(
        self,
        query: str,
        page: int = 1,
        page_size: int = 20,
        sort_by: Optional[str] = None,
    ):
        """Search products using a textual query.

        :param query: the search query
        :param page: requested page (starts at 1), defaults to 1
        :param page_size: number of items per page, defaults to 20
        :param sort_by: result sorting key, defaults to None (no sorting)
        :return: the search results
        """
        # We force usage of v2 of API
        params = {
            "search_terms": query,
            "page": page,
            "page_size": page_size,
            "sort_by": sort_by,
            "json": "1",
        }

        if sort_by is not None:
            params["sort_by"] = sort_by

        return send_get_request(
            url=f"{self.base_url}/api/v2/search",
            api_config=self.api_config,
            params=params,
        )

    def update(self, body: Dict[str, Any]):
        """Create a new product or create it if it doesn't exist yet."""
        if not body.get("code"):
            raise ValueError("missing code from body")

        url = f"{self.base_url}/cgi/product_jqm2.pl"
        return send_for_urlencoded_post_request(url, body, self.api_config)

    def select_image(
        self,
        code: str,
        image_id: str,
        image_key: str,
        rotate: Optional[int] = None,
        crop_bounding_box: Optional[tuple[float, float, float, float]] = None,
    ):
        """Select an image (front/ingredients/nutrition/packaging) for a
        product.

        It's possible to rotate and crop the selection.

        :param code: the product barcode
        :param image_id: the raw image ID, it must be a digit (ex: 1, 2, 3, 4)
        :param image_key: the image field name (one of `front`, `ingredients`,
            `nutrition`, `packaging`) and the language code, separated by a
            `_`. Example: `front_fr`, `ingredients_en`, `nutrition_es`, etc.
        :param rotate: rotation angle in degrees (90, 180, 270), defaults to
            None (no rotation)
        :param crop_bounding_box: a tuple of 4 floats
            (y_min, x_min, y_max, x_max) that defines the bounding box of the
            crop, defaults to None (no crop)
        :raises ValueError: if the rotation angle is invalid or if no password
            or session cookie is provided
        :return: the API response
        """
        url = f"{self.base_url}/cgi/product_image_crop.pl"
        params: JSONType = {
            "code": code,
            "imgid": image_id,
            # We need to tell Product Opener that the bounding box coordinates
            # are related to the full image
            "coordinates_image_size": "full",
        }

        if rotate is not None and rotate != 0:
            if rotate not in (90, 180, 270):
                raise ValueError(f"invalid value for rotation angle: {rotate}")
            params["angle"] = str(rotate)

        if crop_bounding_box is not None:
            y_min, x_min, y_max, x_max = crop_bounding_box
            params["x1"] = x_min
            params["y1"] = y_min
            params["x2"] = x_max
            params["y2"] = y_max

        if image_key is not None:
            params["id"] = image_key

        cookies = None
        if self.api_config.session_cookie:
            cookies = {
                "session": self.api_config.session_cookie,
            }
        elif self.api_config.username:
            params["user_id"] = self.api_config.username
            params["password"] = self.api_config.password

        if cookies is None and not params.get("password"):
            raise ValueError(
                "a password or a session cookie is required to select an image"
            )

        r = http_session.post(
            url,
            data=params,
            timeout=self.api_config.timeout,
            auth=get_http_auth(self.api_config.environment),
            cookies=cookies,
        )

        r.raise_for_status()
        return r


class API:
    def __init__(
        self,
        username: Optional[str] = None,
        password: Optional[str] = None,
        country: Union[Country, str] = Country.world,
        flavor: Union[Flavor, str] = Flavor.off,
        version: Union[APIVersion, str] = APIVersion.v2,
        environment: Union[Environment, str] = Environment.org,
        session_cookie: Optional[str] = None,
    ) -> None:
        """Initialize the API instance.

        :param username: user username, only used for write requests, defaults
            to None
        :param password: user password, only used for write requests, defaults
            to None
        :param country: the country, has an effect on the default display
            language and when uploading products, defaults to Country.world
        :param flavor: which O*F project to use, defaults to Flavor.off (Open
            Food Facts)
        :param version: the API version to use, defaults to APIVersion.v2
        :param environment: what environment (prod/staging) to use, defaults
            to Environment.org
        :param session_cookie: a session cookie, only used for write requests,
            defaults to None
        """
        if not isinstance(country, Country):
            country = Country[country]

        self.api_config = APIConfig(
            country=country,
            flavor=Flavor[flavor],
            version=APIVersion[version],
            environment=Environment[environment],
            username=username,
            password=password,
            session_cookie=session_cookie,
        )
        self.password = password
        self.country = country
        self.product = ProductResource(self.api_config)
        self.facet = FacetResource(self.api_config)
