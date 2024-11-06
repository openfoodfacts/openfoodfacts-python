import re

import pytest

from openfoodfacts.taxonomy import (
    Taxonomy,
    TaxonomyNode,
    create_taxonomy_mapping,
    map_to_canonical_id,
)


def test_map_to_canonical_id():
    taxonomy_mapping = {
        "en:apple": "en:apples",
        "en:apples": "en:apples",
        "fr:pomme": "en:apples",
        "fr:noix-d-isere": "en:nuts-from-isere",
    }
    values = [
        "en: Apple",
        "en: apples",
        "fr: Pomme",
        "fr: Bananes d'Isère",
        "fr: Noix d'Isère",
    ]
    expected = {
        "en: Apple": "en:apples",
        "en: apples": "en:apples",
        "fr: Pomme": "en:apples",
        "fr: Bananes d'Isère": "fr:bananes-d-isere",
        "fr: Noix d'Isère": "en:nuts-from-isere",
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
        taxonomy.add(node1.id, node1)
        taxonomy.add(node2.id, node2)

        expected_mapping = {
            "en:apple": "en:apples",
            "fr:pomme": "en:apples",
            "en:apples": "en:apples",
            "fr:pommes": "en:apples",
            "fr:noix-d-isere": "en:nuts-from-isere",
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
