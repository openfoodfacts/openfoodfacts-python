# 📖 Usage Guide

This guide provides a comprehensive overview of the Open Food Facts Python SDK —
covering setup, product search, facets, ingredient analysis, and dataset access.

> 🔗 **Official Resources:**
> [API Documentation](https://openfoodfacts.github.io/openfoodfacts-server/api/) |
> [Open Food Facts](https://world.openfoodfacts.org/) |
> [GitHub Repository](https://github.com/openfoodfacts/openfoodfacts-python)

---

## ⚡ Quick Examples

Get started in seconds — no configuration needed for read-only access:

```python
import openfoodfacts

api = openfoodfacts.API(user_agent="MyApp/1.0")

# Get a product by barcode
print(api.product.get("3017620422003")["product_name"])
# → "Nutella"

# Search for products
results = api.product.text_search("pizza")
print(f"Found {results['count']} products")

# Get all organic products
organic = api.facet.get_products("label", "en:organic")
print(organic["products"][0]["product_name"])
```

---

## 🚀 Setup

### Installation

```bash
pip install openfoodfacts
```

### Initialize the API

```python
from openfoodfacts import API, APIVersion, Country, Environment, Flavor

api = API(
    user_agent="MyAwesomeApp/1.0",  # required — describe your app/script
    username=None,                   # optional — needed for write requests
    password=None,                   # optional — needed for write requests
    country=Country.world,           # optional — filters by country
    flavor=Flavor.off,               # optional — which Open*Facts project
    version=APIVersion.v2,           # optional — use v3 for advanced features
    environment=Environment.org,     # optional — org=production, net=staging
    timeout=30,                      # optional — seconds before request fails
)
```

### Configuration Parameters

| Parameter    | Description                                                                 | Default  |
|--------------|-----------------------------------------------------------------------------|----------|
| `user_agent` | Identifies your app in HTTP requests. **Required.**                         | —        |
| `username`   | Your OFF account username, needed for write requests                        | `None`   |
| `password`   | Your OFF account password, needed for write requests                        | `None`   |
| `country`    | Filters products by country and infers display language                     | `world`  |
| `flavor`     | Which Open\*Facts project: `off`, `obf`, `opff`, `opf`                     | `off`    |
| `version`    | API version: `v2` (default, stable) or `v3` (required for some features)   | `v2`     |
| `environment`| `org` = production (stable) · `net` = staging (for testing/development)    | `org`    |
| `timeout`    | Request timeout in seconds. Increase if you experience timeout errors.      | `10`     |

> ℹ️ **API Version Note:** Most read operations work on `v2`. However, some features
> like ingredient parsing and image upload **require `v3`**. These are noted in each section below.

---

## 🔍 Products

### Get a product by barcode

```python
code = "3017620422003"
product = api.product.get(code)

print(product["product_name"])  # → "Nutella"
```

Request only specific fields to speed up the response:

```python
product = api.product.get(
    code,
    fields=["code", "product_name", "brands", "nutriscore_grade"]
)
```

If the product doesn't exist, `None` is returned:

```python
product = api.product.get("0000000000000")
if product is None:
    print("Product not found")
```

---

### Text Search

```python
# Basic search
results = api.product.text_search("pizza")

# Control pagination and page size
results = api.product.text_search("pizza", page=1, page_size=20)

# Access the list of products
products = results["products"]
for product in products:
    # dict.get(key, default) safely returns "Unknown" if the key is missing
    print(product.get("product_name", "Unknown"))
```

> 💡 **Response fields:**
>
> | Field                  | Description                            |
> |------------------------|----------------------------------------|
> | `results["products"]`  | List of matching product dicts         |
> | `results["count"]`     | Total number of matching products      |
> | `results["page"]`      | Current page number                    |
> | `results["page_size"]` | Number of results returned on this page|

---

### Create or Update a Product

> ⚠️ Requires `username` and `password` to be set in the API config.

```python
api.product.update({
    "code":                 "3850334341389",
    "product_name":         "Mlinci",
    "ingredients_text_en":  "wheat flour, water, salt",
    # You can also update other fields when authenticated:
    "categories_tags":      "en:pastas",
    "labels_tags":          "en:no-preservatives",
    "brands":               "My Brand",
})
```

For a full list of updatable fields, see the
[Open Food Facts Write API docs](https://openfoodfacts.github.io/openfoodfacts-server/api/).

---

### Ingredient Analysis

> ⚠️ **Requires `APIVersion.v3`.**  
> Only available for the `off` (Open Food Facts) flavor.  
> Prefer using `Environment.net` (staging) to avoid overloading production.

```python
from openfoodfacts import API, APIVersion, Environment

api = API(
    user_agent="MyAwesomeApp/1.0",
    version=APIVersion.v3,       # v3 required for ingredient parsing
    environment=Environment.net, # use staging for costly operations
)

ingredients = api.product.parse_ingredients("water, sugar, salt", lang="en")

for item in ingredients:
    print(f"{item['text']:10} → {item['id']:15} ({item['percent_estimate']:.1f}%)")
# water      → en:water         (66.7%)
# sugar      → en:sugar         (16.7%)
# salt       → en:salt          (16.7%)
```

<details>
<summary>📄 View full example response</summary>

```python
[
  {
    'ciqual_food_code':   '18066',
    'ecobalyse_code':     'tap-water',
    'id':                 'en:water',
    'is_in_taxonomy':     1,
    'percent_estimate':   66.6666666666667,
    'percent_max':        100,
    'percent_min':        33.3333333333333,
    'text':               'water',
    'vegan':              'yes',
    'vegetarian':         'yes'
  },
  {
    'ciqual_proxy_food_code': '31016',
    'ecobalyse_code':         'sugar',
    'id':                     'en:sugar',
    'is_in_taxonomy':         1,
    'percent_estimate':       16.6666666666667,
    'percent_max':            50,
    'percent_min':            0,
    'text':                   'sugar',
    'vegan':                  'yes',
    'vegetarian':             'yes'
  },
  {
    'ciqual_food_code':  '11058',
    'id':                'en:salt',
    'is_in_taxonomy':    1,
    'percent_estimate':  16.6666666666667,
    'percent_max':       33.3333333333333,
    'percent_min':       0,
    'text':              'salt',
    'vegan':             'yes',
    'vegetarian':        'yes'
  }
]
```

</details>

---

## 🏷️ Facets

Facets let you retrieve all possible values for a given attribute —
such as brands, categories, labels, packaging types, and countries.

### Get facet values

```python
# Get all brands — page 1, 20 results by default
results = api.facet.get("brand")

# Customize page size (how many results to return at once)
results = api.facet.get("brand", page=1, page_size=50)

# Paginate to the next page
results_page2 = api.facet.get("brand", page=2, page_size=50)
```

> ⚠️ **Result Limit:** The API returns a maximum of **10,000 results** per request.
> Use the `page` parameter to paginate through large datasets.
> For full bulk access, download the dataset directly:
> 👉 https://world.openfoodfacts.org/data

---

### Get products for a specific facet value

```python
# Get products labelled "en:organic"
results = api.facet.get_products("label", "en:organic", page=1, page_size=25)

# Access the list of products
products = results["products"]
for product in products:
    print(product.get("product_name", "Unknown"))

# Sort by popularity
results = api.facet.get_products(
    "label", "en:organic",
    sort_by="popularity"   # other options: "last_modified_t", "created_t"
)
```

---

## 📦 Dataset

For large-scale data analysis, download the full Open Food Facts dataset —
it's faster and more complete than paginating through the API.

```python
from openfoodfacts import ProductDataset

# Automatically downloads and caches the CSV dataset on first use
dataset = ProductDataset(dataset_type="csv")

for product in dataset:
    print(product["product_name"])
```

### Dataset types

| Type   | Size    | Contents                        | Best for              |
|--------|---------|---------------------------------|-----------------------|
| `csv`  | ~800 MB | Most important fields only      | Quick analysis        |
| `jsonl`| >5 GB   | Full database — all fields      | Complete data science |

> 💡 The dataset is **automatically downloaded and cached** on first use.

---

## ⚠️ Error Handling

The SDK raises standard exceptions for network or API errors. Always wrap requests in a `try/except` block in production code:

```python
import requests

try:
    product = api.product.get("3017620422003")

    if product is None:
        print("Product not found (barcode may be invalid or not in database)")
    else:
        print(product["product_name"])

except requests.exceptions.Timeout:
    print("Request timed out — try increasing the timeout value in API config")

except requests.exceptions.ConnectionError:
    print("Network error — check your internet connection")

except requests.exceptions.HTTPError as e:
    print(f"HTTP error: {e.response.status_code} — {e.response.text}")
```

---

## 💡 FAQ & Common Gotchas

**Q: Do I need an API key?**  
No. The Open Food Facts API is free and open — no API key required for read operations.
Authentication (`username` + `password`) is only needed for write operations.

**Q: Are there rate limits?**  
The API does not enforce strict rate limits, but please be respectful — avoid sending
thousands of requests per second. For bulk data needs, use the **dataset download** instead.

**Q: My request keeps timing out. What should I do?**  
Increase the `timeout` parameter when creating the API object (e.g., `timeout=60`).
For large dataset operations, use `ProductDataset` instead of the API.

**Q: I'm getting garbled text / encoding issues. Why?**  
Product names and ingredients are stored in UTF-8. Make sure your terminal and file
output also use UTF-8 encoding. In Python 3 this is the default, but some Windows
terminals may need `chcp 65001` to display UTF-8 correctly.

**Q: Which `version` should I use?**  
Use `APIVersion.v2` for standard product reads and searches.
Use `APIVersion.v3` for ingredient parsing and image uploads.

**Q: What is `Environment.net` for?**  
`Environment.net` points to the **staging server** (openfoodfacts.net). Use it when
testing write operations or costly features like ingredient analysis, so you don't
affect the production database.

---

## 🔬 Taxonomies

Taxonomies define the structured vocabulary used by Open Food Facts —
for categories, labels, ingredients, additives, and more.

For a deep dive on how to work with taxonomies, check out the
[dedicated Taxonomies page](./handle_taxonomies.md) or the
[official taxonomy documentation](https://openfoodfacts.github.io/openfoodfacts-server/api/).