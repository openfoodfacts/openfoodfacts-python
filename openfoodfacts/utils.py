import gzip
import json
import logging
from pathlib import Path
from typing import Callable, Iterable, Optional, Union

import requests

from .types import Environment, Flavor

_orjson_available = True
try:
    import orjson
except ImportError:
    _orjson_available = False

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


def get_logger(name=None, level: Optional[int] = logging.INFO) -> logging.Logger:
    logger = logging.getLogger(name)
    logger.setLevel(level)

    if name is None:
        configure_root_logger(logger, level)

    return logger


def configure_root_logger(
    logger: logging.Logger,
    level: int = logging.INFO,
    formatter_string: Optional[str] = None,
):
    logger.setLevel(level)
    handler = logging.StreamHandler()

    if formatter_string is None:
        formatter_string = "%(asctime)s :: %(levelname)s :: %(message)s"

    formatter = logging.Formatter(formatter_string)
    handler.setFormatter(formatter)
    handler.setLevel(level)
    logger.addHandler(handler)
    return logger


def jsonl_iter(jsonl_path: Union[str, Path]) -> Iterable[dict]:
    """Iterate over elements of a JSONL file.

    :param jsonl_path: the path of the JSONL file. Both plain (.jsonl) and
        gzipped (jsonl.gz) files are supported.
    :yield: dict contained in the JSONL file
    """
    open_fn = get_open_fn(jsonl_path)

    with open_fn(str(jsonl_path), "rt", encoding="utf-8") as f:
        yield from jsonl_iter_fp(f)


def get_open_fn(filepath: Union[str, Path]) -> Callable:
    filepath = str(filepath)
    if filepath.endswith(".gz"):
        return gzip.open
    else:
        return open


def jsonl_iter_fp(fp) -> Iterable[dict]:
    for line in fp:
        line = line.strip("\n")
        if line:
            if _orjson_available:
                yield orjson.loads(line)
            else:
                yield json.loads(line)
