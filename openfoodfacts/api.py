from typing import Any, Dict, List, Optional, Tuple, Union

import requests

from .types import APIConfig, APIVersion, Country, Environment, Facet, Flavor
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


class API:
    def __init__(
        self,
        username: Optional[str] = None,
        password: Optional[str] = None,
        country: Union[Country, str] = Country.world,
        flavor: Union[Flavor, str] = Flavor.off,
        version: Union[APIVersion, str] = APIVersion.v2,
        environment: Union[Environment, str] = Environment.org,
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
        """
        if not isinstance(country, Country):
            country = Country.get_from_2_letter_code(country)

        self.api_config = APIConfig(
            country=country,  # type: ignore
            flavor=Flavor[flavor],
            version=APIVersion[version],
            environment=Environment[environment],
            username=username,
            password=password,
        )
        self.password = password
        self.country = country
        self.product = ProductResource(self.api_config)
        self.facet = FacetResource(self.api_config)
