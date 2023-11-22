# Handle taxonomies

The Python SDK provides an easy way to access and handle the taxonomies available on Open Food Facts.

Taxonomies are at the heart of Open Food Facts. They are used to structure knowledge about ingredients, categories, labels, additives, countries, brands, etc.

To have a better understanding of how taxonomies work, you can read the [wiki page about taxonomies](https://wiki.openfoodfacts.org/Global_taxonomies).

## Usage

### Get information about a taxonomy item

First, instantiate a Taxonomy object:

```python
from openfoodfacts.taxonomy import get_taxonomy

# Use the singular form of the taxonomy name
taxonomy = get_taxonomy("category")
print(taxonomy)
# <openfoodfacts.taxonomy.Taxonomy object at 0x7fe9d3f44940>
```

The taxonomy object provides a way to access the taxonomy data. For example, if you want to get the node `en:biscuits`:

```python
node = taxonomy["en:biscuits"]
print(node)
# <TaxonomyNode en:biscuits>
```

If the node does not exist, `None` is returned.

You can get the the translation in a specific language:

```python
print(node.get_localized_name("it"))
# Biscotti
```

Each node has one or more parents, stored in the `parents` field:

```python
print(node.parents)
# [<TaxonomyNode en:biscuits-and-cakes>]
```

Likewise, children can be accessed using the `children` field.


To get the full parent hierarchy (that includes all parents found recursively), use the `get_parents_hierarchy` method:

```python
print(node.get_parents_hierarchy())
# [<TaxonomyNode en:biscuits-and-cakes>, <TaxonomyNode en:sweet-snacks>, <TaxonomyNode en:snacks>]
```

Beside the main translation that can be accessed using `get_localized_name`, each node may have synonyms. This information can be easily accessed as well:

```python
# synonyms is a dict mapping language codes to a list of
# synonyms in that language. The key is missing if there are
# no synonyms.
print(node.synonyms["es"])
# ["Galletas", "galleta"]
```

Taxonomy node properties are stored in the `properties` field:

```python
print(node.properties)
# {
#    "wikipedia": {"en": "https://en.wikipedia.org/wiki/Biscuit"},
#    "carbon_footprint_fr_foodges_ingredient": {"fr": "Biscuit au beurre"},
#    "agribalyse_proxy_food_code": {"en": "24000"},
#    "ciqual_proxy_food_name": {
#        "en": "Biscuit -cookie-",
#        "fr": "Biscuit sec, sans précision",
#    },
#    "wikidata": {"en": "Q13270"},
#    "ciqual_proxy_food_code": {"en": "24000"},
#}
```

### The Taxonomy object

The `Taxonomy` object is a dictionary-like object that maps node IDs to `TaxonomyNode` objects.

It also provides a way to iterate over all nodes:

```python
for node in taxonomy.iter_nodes():
    print(node)
# <TaxonomyNode fr:beaune-premier-cru-belissand-blanc>
# <TaxonomyNode fr:pommard-les-rugiens-bas>
# <TaxonomyNode en:hazelnut-butters>
# <TaxonomyNode fr:pernand-vergelesses>
# <TaxonomyNode it:terre-di-pisa>
# <TaxonomyNode en:creamy-quark>
# ...
```

#### Find leaf nodes in the taxonomy

One very common usecase is to find the leafs nodes among a list of nodes, i.e. the nodes that have no children.
For example, in Open Food Facts, the `categories_tags` field contains the categories submitted by the user and all their parents. If you're only interested in the most precise categories, you need to filter out the categories that have children:

```python
# Let's say you have a product that has the following categories:
categories_tags = ["en:plant-based-foods-and-beverages","en:plant-based-foods","en:breakfasts","en:cereals-and-potatoes","en:fruits-and-vegetables-based-foods","en:cereals-and-their-products","en:fruits-based-foods","en:breakfast-cereals","en:mueslis","en:cereals-with-nuts","en:crunchy-cereal-clusters","en:cereal-clusters-with-nuts"]

# Convert the ID to TaxonomyNode objects:
categories_nodes = [taxonomy[tag] for tag in categories_tags if tag in taxonomy]

# Let's find the leaf nodes using find_deepest_nodes method:
leaf_nodes = taxonomy.find_deepest_nodes(categories_nodes)
print(leaf_nodes)
# [<TaxonomyNode en:fruits-based-foods>, <TaxonomyNode en:mueslis>, <TaxonomyNode en:cereal-clusters-with-nuts>]
```

As you can see, the parent categories were removed, and only the leaf nodes remain.