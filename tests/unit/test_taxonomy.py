import re

import pytest

from openfoodfacts.taxonomy import (
    Taxonomy,
    TaxonomyNode,
    create_brand_taxonomy_mapping,
    create_taxonomy_mapping,
    get_taxonomy,
    map_to_canonical_id,
)

label_taxonomy = get_taxonomy("label")
category_taxonomy = get_taxonomy("category")


def test_map_to_canonical_id():
    taxonomy_mapping = {
        "en:apple": "en:apples",
        "en:apples": "en:apples",
        "fr:pomme": "en:apples",
        "fr:noix-d-isere": "en:nuts-from-isere",
        "xx:provence-alpes-cote-d-azur": "en:provence-alpes-cote-d-azur",
        "xx:sashimi": "xx:sashimi",
    }
    values = [
        "en: Apple",
        "en: apples",
        "fr: Pomme",
        "fr: Bananes d'Isère",
        "fr: Noix d'Isère",
        "fr: Provence-Alpes-Côte d'Azur",
        "pt: Provence-Alpes-Côte d'Azur",
        "it: sashimi",
    ]
    expected = {
        "en: Apple": "en:apples",
        "en: apples": "en:apples",
        "fr: Pomme": "en:apples",
        "fr: Bananes d'Isère": "fr:bananes-d-isere",
        "fr: Noix d'Isère": "en:nuts-from-isere",
        "fr: Provence-Alpes-Côte d'Azur": "en:provence-alpes-cote-d-azur",
        "pt: Provence-Alpes-Côte d'Azur": "en:provence-alpes-cote-d-azur",
        "it: sashimi": "xx:sashimi",
    }
    assert map_to_canonical_id(taxonomy_mapping, values) == expected


def test_map_to_canonical_id_invalid_value():
    taxonomy_mapping = {
        "en:apple": "en:apples",
        "en:apples": "en:apples",
        "fr:pomme": "en:apples",
        "fr:noix-d-isere": "en:nuts-from-isere",
    }
    values = ["en: Apple", "apple"]

    with pytest.raises(
        ValueError,
        match=re.escape(
            "Invalid value: 'apple', expected value to be in 'lang:tag' format"
        ),
    ):
        map_to_canonical_id(taxonomy_mapping, values)


class TestCreateTaxonomyMapping:
    def test_basic(self):
        taxonomy = Taxonomy()
        node1 = TaxonomyNode(
            identifier="en:apples",
            names={"en": "Apple", "fr": "Pomme"},
            synonyms={"en": ["Apples"], "fr": ["Pommes"]},
        )
        node2 = TaxonomyNode(
            identifier="en:nuts-from-isere",
            names={"fr": "Noix d'Isère"},
            synonyms={"fr": ["Noix d'Isère"]},
        )
        node3 = TaxonomyNode(
            identifier="xx:sashimi",
            names={"xx": "Sashimi"},
            synonyms={"xx": ["Sashimi"]},
        )
        taxonomy.add(node1.id, node1)
        taxonomy.add(node2.id, node2)
        taxonomy.add(node3.id, node3)

        expected_mapping = {
            "en:apple": "en:apples",
            "fr:pomme": "en:apples",
            "en:apples": "en:apples",
            "fr:pommes": "en:apples",
            "fr:noix-d-isere": "en:nuts-from-isere",
            "xx:sashimi": "xx:sashimi",
        }

        assert create_taxonomy_mapping(taxonomy) == expected_mapping

    def test_empty(self):
        taxonomy = Taxonomy()
        expected_mapping = {}
        assert create_taxonomy_mapping(taxonomy) == expected_mapping

    def test_no_synonyms(self):
        taxonomy = Taxonomy()
        node = TaxonomyNode(
            identifier="en:bananas",
            names={"en": "Banana", "fr": "Banane"},
            synonyms={},
        )
        taxonomy.add(node.id, node)

        expected_mapping = {
            "en:banana": "en:bananas",
            "fr:banane": "en:bananas",
        }

        assert create_taxonomy_mapping(taxonomy) == expected_mapping

    def test_multiple_languages_with_different_synonyms(self):
        taxonomy = Taxonomy()
        node = TaxonomyNode(
            identifier="en:grapes",
            names={"en": "Grape", "fr": "Raisin", "es": "Uva"},
            synonyms={
                "en": ["Grapes"],
                "fr": ["Raisins", "Raisins d'automne"],
                "es": ["Uvas"],
            },
        )
        taxonomy.add(node.id, node)

        expected_mapping = {
            "en:grape": "en:grapes",
            "fr:raisin": "en:grapes",
            "fr:raisins-d-automne": "en:grapes",
            "es:uva": "en:grapes",
            "en:grapes": "en:grapes",
            "fr:raisins": "en:grapes",
            "es:uvas": "en:grapes",
        }

        assert create_taxonomy_mapping(taxonomy) == expected_mapping

    def test_create_brand_taxonomy_mapping(self):
        taxonomy = Taxonomy.from_dict(
            {
                "en:5th-season": {"name": {"en": "5th Season"}},
                "en:arev": {"name": {"en": "Arèv"}},
                "en:arrighi": {"name": {"en": "Arrighi"}},
                "en:voiles-au-vent": {"name": {"en": "Voiles au Vent"}},
                "xx:turini": {"name": {"xx": "Turini"}},
                "fr:auchan": {"name": {"xx": "Auchan"}},
                "fr:mamouth": {"name": {"fr": "Mamouth"}},
                "fr:carefour": {"name": {}},
            }
        )
        assert create_brand_taxonomy_mapping(taxonomy) == {
            "5th-season": "5th Season",
            "arev": "Arèv",
            "arrighi": "Arrighi",
            "voiles-au-vent": "Voiles au Vent",
            "turini": "Turini",
            "auchan": "Auchan",
            "mamouth": "Mamouth",
            "carefour": "carefour",
        }


class TestTaxonomy:
    @pytest.mark.parametrize(
        "taxonomy,item,candidates,output",
        [
            (label_taxonomy, "en:organic", {"en:fr-bio-01"}, True),
            (label_taxonomy, "en:fr-bio-01", {"en:organic"}, False),
            (label_taxonomy, "en:fr-bio-01", [], False),
            (label_taxonomy, "en:organic", {"en:gluten-free"}, False),
            (
                label_taxonomy,
                "en:organic",
                {"en:gluten-free", "en:no-additives", "en:vegan"},
                False,
            ),
            (
                label_taxonomy,
                "en:organic",
                {"en:gluten-free", "en:no-additives", "en:fr-bio-16"},
                True,
            ),
        ],
    )
    def test_is_child_of_any(
        self, taxonomy: Taxonomy, item: str, candidates: list, output: bool
    ):
        assert taxonomy.is_parent_of_any(item, candidates) is output

    def test_is_child_of_any_unknwon_item(self):
        with pytest.raises(ValueError):
            label_taxonomy.is_parent_of_any("unknown-id", set())

    @pytest.mark.parametrize(
        "taxonomy,item,output",
        [
            (category_taxonomy, "en:plant-based-foods-and-beverages", set()),
            (
                category_taxonomy,
                "en:plant-based-foods",
                {"en:plant-based-foods-and-beverages"},
            ),
            (
                category_taxonomy,
                "en:brown-rices",
                {
                    "en:rices",
                    "en:cereal-grains",
                    "en:cereals-and-their-products",
                    "en:cereals-and-potatoes",
                    "en:plant-based-foods",
                    "en:plant-based-foods-and-beverages",
                    "en:seeds",
                },
            ),
        ],
    )
    def test_get_parents_hierarchy(
        self, taxonomy: Taxonomy, item: str, output: set[str]
    ):
        node = taxonomy[item]
        parents = node.get_parents_hierarchy()
        assert set((x.id for x in parents)) == output

    @pytest.mark.parametrize(
        "taxonomy,items,output",
        [
            (category_taxonomy, [], []),
            (category_taxonomy, ["en:brown-rices"], ["en:brown-rices"]),
            (category_taxonomy, ["en:brown-rices", "en:rices"], ["en:brown-rices"]),
            (
                category_taxonomy,
                ["en:brown-rices", "en:rices", "en:cereal-grains"],
                ["en:brown-rices"],
            ),
            (
                category_taxonomy,
                ["en:brown-rices", "en:teas", "en:cereal-grains"],
                ["en:brown-rices", "en:teas"],
            ),
        ],
    )
    def test_find_deepest_nodes(
        self, taxonomy: Taxonomy, items: list[str], output: list[str]
    ):
        item_nodes = [taxonomy[item] for item in items]
        output_nodes = [taxonomy[o] for o in output]
        assert taxonomy.find_deepest_nodes(item_nodes) == output_nodes
