# Usage Guide

This guide provides information on the methods available within the Open Food Facts Python SDK.

## API

The SDK can be used to access Open Food Facts API.

First, instantiate an API object:

```python
from openfoodfacts import API, APIVersion, Country, Environment, Flavor

api = API(
    user_agent="<application name>",
    username=None,
    password=None,
    country=Country.world,
    flavor=Flavor.off,
    version=APIVersion.v2,
    environment=Environment.org,
)
```

All parameters are optional with the exception of user_agent, but here is a description of the parameters you can tweak:

- `username` and `password` are used to provide authentication (required for write requests)
- `country` is used to specify the country, which is used by the API to return product specific to the country or to infer which language to use by default. `world` (all products) is the default value
- `flavor`: the Open*Facts project you want to interact with: `off` (Open Food Facts, default), `obf` (Open Beauty Facts), `opff` (Open Pet Food Facts), `opf` (Open Products Facts)
- `version`: API version (v2 is the default)
- `environment`: either `org` for production environment (openfoodfacts.org) or `net` for staging (openfoodfacts.net)

### Get information about a product

```python
code = "3017620422003"
api.product.get(code)
```

### Perform text search

```python
results = api.product.text_search("pizza")
```

### Create a new product or update an existing one

```python
results = api.product.update(body)
```

with `body` the update body. It is a dictionary. It should contain 
the key "code" and its value, corresponding to the product that we
want to update. Example:
```body = {'code': '3850334341389', 'product_name': 'Mlinci'}```

### Perform ingredient analysis

You can perform the ingredient analysis of a text in a given language using the API. Please note that ingredient analysis is costly, so prefer using the preprod server for this operation.

```python
from openfoodfacts import API, APIVersion, Environment

api = API(user_agent="<application name>",
          version=APIVersion.v3,
          environment=Environment.net)

results = api.product.parse_ingredients("water, sugar, salt", lang="en")

print(results)

## [{'ciqual_food_code': '18066',
#  'ecobalyse_code': 'tap-water',
#  'id': 'en:water',
#  'is_in_taxonomy': 1,
#  'percent_estimate': 66.6666666666667,
#  'percent_max': 100,
#  'percent_min': 33.3333333333333,
#  'text': 'water',
#  'vegan': 'yes',
#  'vegetarian': 'yes'},
# {'ciqual_proxy_food_code': '31016',
#  'ecobalyse_code': 'sugar',
#  'id': 'en:sugar',
#  'is_in_taxonomy': 1,
#  'percent_estimate': 16.6666666666667,
#  'percent_max': 50,
#  'percent_min': 0,
#  'text': 'sugar',
#  'vegan': 'yes',
#  'vegetarian': 'yes'},
# {'ciqual_food_code': '11058',
#  'id': 'en:salt',
#  'is_in_taxonomy': 1,
#  'percent_estimate': 16.6666666666667,
#  'percent_max': 33.3333333333333,
#  'percent_min': 0,
#  'text': 'salt',
#  'vegan': 'yes',
#  'vegetarian': 'yes'}]
```

## Using the dataset

If you're planning to perform data analysis on Open Food Facts, the easiest way is to download and use the Open Food Facts dataset dump. Fortunately it can be done really easily using the SDK:

```python
from openfoodfacts import ProductDataset

dataset = ProductDataset(dataset_type="csv")

for product in dataset:
    print(product["product_name"])
```

With `dataset = ProductDataset(dataset_type="csv")`, we automatically download (and cache) the food dataset. We can then iterate over it to get information about products.

Two dataset types are available `csv` and `jsonl`. The `jsonl` dataset contains all the Open Food Facts database information but takes much more storage (>5 GB), while the `csv` dataset is much ligher (~800 MB) but only contains the most important fields. The `jsonl` dataset type is used by default.

You can also use `ProductDataset` to fetch other non-food datasets:

```python
from openfoodfacts import ProductDataset

dataset = ProductDataset(dataset_type="csv")

for product in dataset:
    print(product["product_name"])
```

## Taxonomies

For a deep dive on how to handle taxonomies, check out the [dedicated page](./handle_taxonomies.md).
