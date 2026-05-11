import pytest

from openfoodfacts.types import (
    Flavor,
    JSONType,
    NutritionV3,
    NutritionV3InputSet,
    NutritionV3NutrientInput,
    TaxonomyType,
)


class TestFlavor:
    def test_str(self):
        assert str(Flavor.off) == "off"

    def test_from_product_type_food(self):
        assert Flavor.from_product_type("food") == Flavor.off

    def test_from_product_type_beauty(self):
        assert Flavor.from_product_type("beauty") == Flavor.obf

    def test_from_product_type_petfood(self):
        assert Flavor.from_product_type("petfood") == Flavor.opff

    def test_from_product_type_product(self):
        assert Flavor.from_product_type("product") == Flavor.opf

    def test_from_product_type_invalid(self):
        with pytest.raises(
            ValueError, match="no Flavor matched with product_type 'invalid'"
        ):
            Flavor.from_product_type("invalid")


class TestTaxonomyType:
    def test_str(self):
        assert str(TaxonomyType.category) == "category"

    def test_type_unknown(self):
        with pytest.raises(AttributeError):
            _ = TaxonomyType.unknown

    def test_dataset_path_known(self):
        assert (
            TaxonomyType.category.dataset_path == "data/taxonomies/categories.full.json"
        )

    def test_dataset_path_unknown(self):
        with pytest.raises(AttributeError):
            _ = TaxonomyType.unknown.dataset_path


NUTRITION_1 = {
    "aggregated_set": {
        "nutrients": {
            "salt": {
                "source": "packaging",
                "source_index": 0,
                "source_per": "serving",
                "unit": "g",
                "value": 0.5,
            },
            "saturated-fat": {
                "source": "packaging",
                "source_index": 0,
                "source_per": "serving",
                "unit": "g",
                "value": 0.5,
            },
        },
        "per": "100g",
        "preparation": "as_sold",
    },
    "input_sets": [
        {
            "nutrients": {
                "salt": {"unit": "g", "value": 1, "value_string": "1"},
                "saturated-fat": {
                    "unit": "g",
                    "value": 1,
                    "value_string": "1",
                },
            },
            "per": "serving",
            "per_quantity": 200,
            "per_unit": "g",
            "preparation": "as_sold",
            "source": "packaging",
        }
    ],
}

NUTRITION_2 = {
    "aggregated_set": {
        "nutrients": {
            "salt": {
                "modifier": "<=",
                "source": "packaging",
                "source_index": 0,
                "source_per": "100g",
                "unit": "g",
                "value": 5,
            },
            "sodium": {
                "modifier": "<=",
                "source": "packaging",
                "source_index": 0,
                "source_per": "100g",
                "unit": "g",
                "value": 2,
            },
            "sugars": {
                "source": "usda",
                "source_index": 1,
                "source_per": "100g",
                "unit": "g",
                "value": 5.2,
            },
        },
        "per": "100g",
        "preparation": "as_sold",
    },
    "input_sets": [
        {
            "nutrients": {
                "sodium": {
                    "modifier": "<=",
                    "unit": "g",
                    "value": 2,
                    "value_string": "2.0",
                }
            },
            "per": "100g",
            "per_quantity": "100",
            "per_unit": "g",
            "preparation": "as_sold",
            "source": "packaging",
        },
        {
            "nutrients": {
                "sodium": {
                    "unit": "g",
                    "value": 0.1,
                    "value_string": "0.1",
                },
                "sugars": {
                    "unit": "g",
                    "value": 5.2,
                    "value_string": "5.2",
                },
            },
            "per": "100g",
            "per_quantity": "100",
            "per_unit": "g",
            "preparation": "as_sold",
            "source": "usda",
        },
    ],
}


# With `value_computed` in the input_set
NUTRITION_3 = {
    "aggregated_set": {
        "nutrients": {
            "carbohydrates": {
                "modifier": "<",
                "source": "packaging",
                "source_index": 0,
                "source_per": "100g",
                "unit": "g",
                "value": 0.5,
            },
            "energy": {
                "source": "packaging",
                "source_index": 0,
                "source_per": "100g",
                "unit": "kJ",
                "value": 332,
                "value_computed": 340.4,
            },
            "energy-kcal": {
                "source": "packaging",
                "source_index": 0,
                "source_per": "100g",
                "unit": "kcal",
                "value": 78,
                "value_computed": 80.3,
            },
            "energy-kj": {
                "source": "packaging",
                "source_index": 0,
                "source_per": "100g",
                "unit": "kJ",
                "value": 332,
                "value_computed": 340.4,
            },
            "fat": {
                "source": "packaging",
                "source_index": 0,
                "source_per": "100g",
                "unit": "g",
                "value": 0.7,
            },
            "proteins": {
                "source": "packaging",
                "source_index": 0,
                "source_per": "100g",
                "unit": "g",
                "value": 18,
            },
            "salt": {
                "source": "packaging",
                "source_index": 0,
                "source_per": "100g",
                "unit": "g",
                "value": 1.2,
            },
            "saturated-fat": {
                "modifier": "<",
                "source": "packaging",
                "source_index": 0,
                "source_per": "100g",
                "unit": "g",
                "value": 0.1,
            },
            "sodium": {
                "modifier": "~",
                "source": "packaging",
                "source_index": 0,
                "source_per": "100g",
                "unit": "g",
                "value": 0.48,
            },
            "sugars": {
                "modifier": "<",
                "source": "packaging",
                "source_index": 0,
                "source_per": "100g",
                "unit": "g",
                "value": 0.5,
            },
        },
        "per": "100g",
        "preparation": "as_sold",
    },
    "input_sets": [
        {
            "nutrients": {
                "carbohydrates": {
                    "modifier": "<",
                    "unit": "g",
                    "value": 0.5,
                    "value_string": "0.5",
                },
                "energy-kcal": {
                    "unit": "kcal",
                    "value": 78,
                    "value_computed": 80.3,
                    "value_string": "78",
                },
                "energy-kj": {
                    "unit": "kJ",
                    "value": 332,
                    "value_computed": 340.4,
                    "value_string": "332",
                },
                "fat": {"unit": "g", "value": 0.7, "value_string": "0.7"},
                "proteins": {"unit": "g", "value": 18, "value_string": "18"},
                "salt": {"unit": "g", "value": 1.2, "value_string": "1.2"},
                "saturated-fat": {
                    "modifier": "<",
                    "unit": "g",
                    "value": 0.1,
                    "value_string": "0.1",
                },
                "sodium": {"unit": "g", "value_computed": 0.48},
                "sugars": {
                    "modifier": "<",
                    "unit": "g",
                    "value": 0.5,
                    "value_string": "0.5",
                },
            },
            "per": "100g",
            "per_quantity": 100,
            "per_unit": "g",
            "preparation": "as_sold",
            "source": "packaging",
            "unspecified_nutrients": ["fiber"],
        }
    ],
}


# With missing er_quantity and per_unit in the input_set
NUTRITION_4 = {
    "input_sets": [
        {
            "last_updated_t": 1771468068,
            "per_unit": "g",
            "source": "packaging",
            "per": "100g",
            "per_quantity": 100,
            "nutrients": {"nova-group": {"unit": "", "value": 4, "value_string": "4"}},
            "preparation": "as_sold",
        },
        {
            "per_unit": "g",
            "source_description": "Estimate from ingredients",
            "preparation": "as_sold",
            "nutrients": {
                "fruits-vegetables-legumes": {
                    "value_string": "0",
                    "unit": "%",
                    "value": 0,
                    "modifier": "~",
                },
                "added-sugars": {
                    "value": 0.182291666666664,
                    "modifier": "~",
                    "unit": "g",
                    "value_string": "0.182291666666664",
                },
                "fruits-vegetables-nuts": {
                    "value_string": "0",
                    "value": 0,
                    "modifier": "~",
                    "unit": "%",
                },
            },
            "per_quantity": 100,
            "per": "100g",
            "source": "estimate",
        },
        {
            "source": "packaging",
            "per": "serving",
            "preparation": "as_sold",
            "nutrients": {
                "energy-kj": {"unit": "kJ", "value_computed": 0},
                "carbohydrates": {"value_string": "0", "unit": "g", "value": 0},
                "energy-kcal": {
                    "value_string": "0",
                    "value": 0,
                    "value_computed": 0,
                    "unit": "kcal",
                },
                "fat": {"value_string": "0", "unit": "g", "value": 0},
                "proteins": {"value_string": "0", "value": 0, "unit": "g"},
            },
        },
    ],
    "aggregated_set": {
        "per": "100g",
        "preparation": "as_sold",
        "nutrients": {
            "fruits-vegetables-legumes": {
                "source_per": "100g",
                "source_index": 1,
                "value": 0,
                "modifier": "~",
                "unit": "%",
                "source": "estimate",
            },
            "added-sugars": {
                "unit": "g",
                "source": "estimate",
                "modifier": "~",
                "value": 0.182291666666664,
                "source_index": 1,
                "source_per": "100g",
            },
            "nova-group": {
                "value": 4,
                "source": "packaging",
                "unit": "",
                "source_per": "100g",
                "source_index": 0,
            },
            "fruits-vegetables-nuts": {
                "modifier": "~",
                "value": 0,
                "source": "estimate",
                "unit": "%",
                "source_per": "100g",
                "source_index": 1,
            },
        },
    },
}


class TestNutritionV3:
    @pytest.mark.parametrize(
        "obj", [NUTRITION_1, NUTRITION_2, NUTRITION_3, NUTRITION_4]
    )
    def test_parse(self, obj: JSONType):
        NutritionV3.model_validate(obj)

    def test_filter_input_sets(self):
        nutrition_obj = NutritionV3.model_validate(NUTRITION_2)
        results = nutrition_obj.filter_input_sets(source="packaging")
        assert len(results) == 1
        assert isinstance(results[0], NutritionV3InputSet)
        assert (
            len(nutrition_obj.filter_input_sets(source="packaging", per="100ml")) == 0
        )

    def test_get_input_nutrient(self):
        nutrition_obj = NutritionV3.model_validate(NUTRITION_2)
        result = nutrition_obj.get_input_nutrient(
            nutrient="sodium",
            per="100g",
            preparation="as_sold",
            per_quantity=100,
            source="packaging",
            per_unit="g",
        )
        assert result is not None
        assert result.value == 2
        assert result.value_string == "2.0"
        assert result.unit == "g"
        assert result.modifier == "<="

        # We expect no result here
        result = nutrition_obj.get_input_nutrient(
            nutrient="sodium",
            # per was modified here
            per="serving",
            preparation="as_sold",
            per_quantity=100,
            source="packaging",
            per_unit="g",
        )
        assert result is None

        result = nutrition_obj.get_input_nutrient(
            nutrient="sugars",
            source="usda",
        )
        assert result is not None
        assert result.value == 5.2
        assert result.value_string == "5.2"
        assert result.unit == "g"
        assert result.modifier is None


class TestNutritionV3NutrientInput:
    def test_ensure_value_string_is_not_an_int_or_float(self):
        parsed = NutritionV3NutrientInput.model_validate(
            {
                "unit": "g",
                "value": 5.2,
                "value_string": 5.2,
                "modifier": "<",
            }
        )
        assert parsed.value_string == "5.2"
