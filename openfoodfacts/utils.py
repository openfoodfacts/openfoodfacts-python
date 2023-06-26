from typing import Optional

import requests

from .types import Environment, Flavor

http_session = requests.Session()


class URLBuilder:
    """URLBuilder allows to generate URLs for Product Opener/Robotoff.

    Example usage: URLBuilder.robotoff() returns the Robotoff URL.
    """

    @staticmethod
    def _get_url(
        base_domain: str,
        prefix: Optional[str] = "world",
        tld: str = "org",
        scheme: Optional[str] = None,
    ):
        data = {
            "domain": f"{base_domain}.{tld}",
            "scheme": "https",
        }
        if prefix:
            data["prefix"] = prefix
        if scheme:
            data["scheme"] = scheme

        if "prefix" in data:
            return "%(scheme)s://%(prefix)s.%(domain)s" % data

        return "%(scheme)s://%(domain)s" % data

    @staticmethod
    def world(flavor: Flavor, environment: Environment):
        return URLBuilder._get_url(
            prefix="world", tld=environment.value, base_domain=flavor.get_base_domain()
        )

    @staticmethod
    def robotoff(environment: Environment) -> str:
        return URLBuilder._get_url(
            prefix="robotoff",
            tld=environment.value,
            base_domain=Flavor.off.get_base_domain(),
        )

    @staticmethod
    def static(flavor: Flavor, environment: Environment) -> str:
        return URLBuilder._get_url(
            prefix="static", tld=environment.value, base_domain=flavor.get_base_domain()
        )

    @staticmethod
    def image_url(flavor: Flavor, environment: Environment, image_path: str) -> str:
        prefix = URLBuilder._get_url(
            prefix="images", tld=environment.value, base_domain=flavor.get_base_domain()
        )
        return prefix + f"/images/products{image_path}"

    @staticmethod
    def country(flavor: Flavor, environment: Environment, country_code: str) -> str:
        return URLBuilder._get_url(
            prefix=country_code,
            tld=environment.value,
            base_domain=flavor.get_base_domain(),
        )
