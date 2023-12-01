import csv
import enum
import logging
from pathlib import Path
from typing import Annotated, Optional

import redis
import typer

from openfoodfacts import API
from openfoodfacts.api import parse_ingredients
from openfoodfacts.ingredients import add_ingredient_in_taxonomy_field
from openfoodfacts.taxonomy import Taxonomy, get_taxonomy
from openfoodfacts.types import JSONType, TaxonomyType
from openfoodfacts.utils import get_logger, http_session

logger = get_logger()
logger.addHandler(logging.FileHandler("switch_ingredient_lang.log"))


def predict_lang(text: str, k: int = 10, threshold: float = 0.01) -> str:
    r = http_session.get(
        "https://robotoff.openfoodfacts.net/api/v1/predict/lang",
        params={"text": text, "k": k, "threshold": threshold},
    )

    if r.status_code == 400:
        # A HTTP 400 can occur when the query parameter string is too long
        logger.warning("Bad request: %s", r.text)
        return []

    r.raise_for_status()
    data = r.json()
    return data["predictions"]


def log_update(code: str, ingredients_text: str, original_lang: str, new_lang: str):
    output_path = Path("updates.csv")
    add_header = not output_path.exists()

    with open(output_path, "a", newline="") as csvfile:
        fieldnames = ["code", "ingredients_text", "original_lang", "new_lang"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        if add_header:
            writer.writeheader()
        writer.writerow(
            {
                "code": code,
                "ingredients_text": ingredients_text,
                "original_lang": original_lang,
                "new_lang": new_lang,
            }
        )


def update_ingredients(
    api: API,
    code: str,
    original_lang: str,
    new_lang: Optional[str],
    ingredients_text: str,
):
    body = {
        "code": code,
        f"ingredients_text_{original_lang}": "",
    }

    if new_lang is not None:
        body[f"ingredients_text_{new_lang}"] = ingredients_text
        body["comment"] = f"switching lang from '{original_lang}' to '{new_lang}'"
    else:
        body["comment"] = f"removing garbage ingredient list in '{original_lang}'"

    r = api.product.update(body)
    logger.info(f"Response: HTTP {r.status_code}")
    logger.info(r.text)


class LangFixProcessingStatus(str, enum.Enum):
    wrong_quality_tag = enum.auto()
    missing_ingredient_text = enum.auto()
    updated = enum.auto()
    unchanged = enum.auto()
    too_few_ingredients = enum.auto()


def process_product(
    api: API,
    product: JSONType,
    ingredient_taxonomy: Taxonomy,
    confirm: bool = False,
    ingredient_detection_threshold: float = 0.7,
    maximum_fraction_known_ingredients: Optional[float] = None,
) -> LangFixProcessingStatus:
    code = product["code"]
    lang = product["lang"]
    ingredients_lc = product.get("ingredients_lc", lang)
    ingredients_text = product.get(f"ingredients_text_{ingredients_lc}")
    parse_ingredients_original = product["ingredients"]
    (
        original_ingredients_n,
        original_known_ingredients_n,
    ) = add_ingredient_in_taxonomy_field(
        parse_ingredients_original, ingredient_taxonomy
    )

    if original_ingredients_n == 0:
        logger.info("No ingredients found")
        return LangFixProcessingStatus.unchanged

    original_fraction_known_ingredients = (
        original_known_ingredients_n / original_ingredients_n
    )

    if (
        maximum_fraction_known_ingredients is not None
        and original_fraction_known_ingredients > maximum_fraction_known_ingredients
    ):
        logger.info(
            "The ingredient list is already well recognized (%s > %s), skipping",
            original_fraction_known_ingredients,
            maximum_fraction_known_ingredients,
        )
        return LangFixProcessingStatus.wrong_quality_tag

    if original_ingredients_n < 3:
        return LangFixProcessingStatus.too_few_ingredients

    if not ingredients_text:
        logger.info(
            f"Missing ingredients_text_{ingredients_lc} for product {product['code']}"
        )
        return LangFixProcessingStatus.missing_ingredient_text

    logger.info(
        f"Product URL: https://world.openfoodfacts.org/product/{code}, lang: {lang}\n"
        f"ingredients_lc: {ingredients_lc}\ningredients_text: '''{ingredients_text}'''"
    )
    predicted_langs = [
        x for x in predict_lang(ingredients_text, threshold=0.05) if len(x["lang"]) == 2
    ]

    for predicted_lang in predicted_langs:
        predicted_lang_id = predicted_lang["lang"]
        predicted_confidence = predicted_lang["confidence"]

        if predicted_lang_id == ingredients_lc:
            logger.info(
                f"Predicted lang ('{predicted_lang_id}') is the same as ingredients_lc ('{ingredients_lc}')"
            )
            continue

        logger.info(f"Predicted lang: {predicted_lang_id} ({predicted_confidence})")
        parsed_ingredients = parse_ingredients(
            text=ingredients_text,
            lang=predicted_lang_id,
            api_config=api.api_config,
        )
        ingredients_n, known_ingredients_n = add_ingredient_in_taxonomy_field(
            parsed_ingredients, ingredient_taxonomy
        )

        if ingredients_n == 0:
            logger.info("No ingredients found")
            continue

        fraction_known_ingredients = known_ingredients_n / ingredients_n
        logger.info(
            f"% of recognized ingredients: {fraction_known_ingredients * 100}, "
            f"ingredients_n: {ingredients_n}, known_ingredients_n: {known_ingredients_n}"
        )

        if fraction_known_ingredients >= ingredient_detection_threshold:
            confirm_response = (
                typer.confirm(
                    f"Switching lang from '{ingredients_lc}' to '{predicted_lang_id}', confirm?"
                )
                if confirm
                else True
            )
            if confirm_response:
                update_ingredients(
                    api, code, ingredients_lc, predicted_lang_id, ingredients_text
                )
                log_update(code, ingredients_text, ingredients_lc, predicted_lang_id)
                return LangFixProcessingStatus.updated
            else:
                logger.info("Skipping")
                continue

    return LangFixProcessingStatus.unchanged


MAXIMUM_FRACTION_KNOWN_INGREDIENTS = {
    "en:ingredients-100-percent-unknown": 0.0,
    "en:ingredients-80-percent-unknown": 0.2,
    "en:ingredients-60-percent-unknown": 0.4,
    "en:ingredients-40-percent-unknown": 0.6,
    "en:ingredients-20-percent-unknown": 0.8,
}


def main(
    username: Annotated[
        str, typer.Option(envvar="OFF_USERNAME", help="Username to use to login")
    ],
    password: Annotated[
        str, typer.Option(envvar="OFF_PASSWORD", help="Password to use to login")
    ],
    facet_name: str = typer.Option("data_quality_warning", help="Facet name"),
    facet_value: str = typer.Option(
        "en:ingredients-100-percent-unknown", help="Value of the facet"
    ),
    page_size: int = typer.Option(25, help="Number of products to fetch per page"),
    confirm: bool = typer.Option(False, help="Ask for a confirmation before updating"),
    timeout: int = typer.Option(30, help="Timeout for HTTP requests"),
):
    redis_client = redis.Redis(host="localhost", port=6379)
    logger.info(f"Logged in as '{username}'")
    api = API(
        user_agent="Robotoff manual script",
        username=username,
        password=password,
        timeout=timeout,
    )
    ingredient_taxonomy = get_taxonomy(TaxonomyType.ingredient)
    redis_prefix = "ing-fix-100-percent-unknown"
    page = int(redis_client.get(f"{redis_prefix}:start_page") or 1)
    max_page = int(redis_client.get(f"{redis_prefix}:max_page") or 1000)
    total_count = None

    while page < max_page:
        logger.info("Requesting facet page %s", page)
        results = api.facet.get_products(
            facet_name, facet_value, page=page, page_size=page_size
        )
        if total_count is None:
            total_count = api.facet.get_products(
                facet_name, facet_value, page=1, page_size=page_size
            )["count"]

        max_page = total_count // page_size + int(total_count % page_size > 0)
        redis_client.set(f"{redis_prefix}:max_page", max_page)
        products = results["products"]

        for product in products:
            code = product["code"]
            if redis_client.sismember(f"{redis_prefix}:codes", code):
                logger.info(f"Skipping already processed code: {code}")
                continue
            status = process_product(
                api,
                product,
                ingredient_taxonomy,
                confirm=confirm,
                maximum_fraction_known_ingredients=MAXIMUM_FRACTION_KNOWN_INGREDIENTS.get(
                    facet_value
                ),
            )
            redis_client.sadd(f"{redis_prefix}:codes", code)
            redis_client.incr(f"{redis_prefix}:{status.name}")
            redis_client.incr(f"{redis_prefix}:total")

        page += 1
        redis_client.set(f"{redis_prefix}:start_page", page)


if __name__ == "__main__":
    typer.run(main)
