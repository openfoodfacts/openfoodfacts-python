# Usage Guide

This guide provides information on the API. All the I/O is [JSON](www.json.org).

- [Open Food Facts](./Usage.md#open-food-facts)
  - [Login](./Usage.md#login)
  - [Facets](./Usage.md#facets)
  - [Products by Facet](./Usage.md#products-by-facet)
  - [Product](./Usage.md#product)
  - [Search](./Usage.md#search)

- [Open Beauty Facts](./Usage.md#open-beauty-facts)
- [Open Pet Food Facts](./Usage.md#open-pet-food-facts)

## Open Food Facts

#### Login
*Login into Openfoodfacts*

```login_session_object = openfoodfacts.utils.login_into_OFF()```

#### Facets

*Get all available additives.*

```python
traces = openfoodfacts.facets.get_additives()
```

*Get all available allergens.*

```python
allergens = openfoodfacts.facets.get_allergens()
```

*Get all available brands.*

```python
brands = openfoodfacts.facets.get_brands()
```

*Get all available categories.*

```python
categories = openfoodfacts.facets.get_categories()
```

*Get all available countries.*

```python
countries = openfoodfacts.facets.get_countries()
```

*Get all available entry dates.*

```python
entry_dates = openfoodfacts.facets.get_entry_dates()
```

*Get all available ingredients.*

```python
ingredients = openfoodfacts.facets.get_ingredients()
```

*Get all available languages.*

```python
languages = openfoodfacts.facets.get_languages()
```

*Get all available packagings.*

```python
packagings = openfoodfacts.facets.get_packaging()
```

*Get all available packaging codes.*

```python
codes = openfoodfacts.facets.get_packaging_codes()
```

*Get all available purchase places.*

```python
places = openfoodfacts.facets.get_purchase_places()
```

*Get all available stores.*

```python
stores = openfoodfacts.facets.get_stores()
```

*Get all available trace types.*

```python
traces = openfoodfacts.facets.get_traces()
```

*Get all available states.*

```python
states = openfoodfacts.facets.get_states()
```

#### Products by Facet

*Get all products for given facets.*

Page access (pagination) is available through parameters.

```python
products = openfoodfacts.products.get_by_facets({
  'trace': 'egg',
  'country': 'france'
})
```

*Get all products for given additive.*

```python
products = openfoodfacts.products.get_by_additive(additive, page=1)
```

*Get all products for given allergen.*

```python
products = openfoodfacts.products.get_by_allergen(allergen)
```

*Get all products for given brand.*

```python
products = openfoodfacts.products.get_by_brand(brand)
```

*Get all products for given category.*

```python
products = openfoodfacts.products.get_by_category(category)
```

*Get all products for given country.*

```python
products = openfoodfacts.products.get_by_country(country)
```

*Get all products for given entry date.*

```python
products = openfoodfacts.products.get_by_entry_date(entry_date)
```

*Get all products for given ingredient.*

```python
products = openfoodfacts.products.get_by_ingredient(ingredient)
```

*Get all products for given language.*

```python
products = openfoodfacts.products.get_by_language(language)
```

*Get all products for given packaging.*

```python
products = openfoodfacts.products.get_by_packaging(packaging)
```

*Get all products for given packaging code.*

```python
products = openfoodfacts.products.get_by_packaging_code(code)
```

*Get all products for given purchase place.*

```python
products = openfoodfacts.products.get_by_purchase_place(place)
```

*Get all products for given store.*

```python
products = openfoodfacts.products.get_by_store(store)
```

*Get all products for given trace type.*

```python
products = openfoodfacts.products.get_by_trace(trace)
```

*Get all products for given state.*

```python
products = openfoodfacts.products.get_by_state(state)
```


#### Product

*Get a given product.*

```python
product = openfoodfacts.products.get_product(barcode)
```

*Open Food Facts data exports*

```
openfoodfacts.utils.download_data(file_type)
```

*Add a new product.*

```python
status_code = openfoodfacts.products.add_new_product({
  'code': barcode,
  'user_id'  : myUsername,
  'password'  : myPassword,
  'product_name' : myProduct,
  'stores'  : store,
  'brands': brand,
  'packaging': packaging
})
```

*Upload an image.*

```python
status_code = openfoodfacts.products.upload_image(barcode, imagefield, img_path)
```

#### Search

*Basic Search*

```python
search_result = openfoodfacts.products.search(query)
```

*Advanced Search*

Can pass in any [parameters](https://en.wiki.openfoodfacts.org/API/Read/Search#Parameters).

```python
search_result = openfoodfacts.products.advanced_search({
  "search_terms":"coke",
  "tagtype_0":"packaging",
  "tag_contains_0":"contains",
  "tag_0":"plastic",
  "nutriment_0":"energy",
  "nutriment_compare_0":"gt",
  "nutriment_value_0":"0",
  "sort_by":"unique_scans",
  "page_size":"20"
})
```

## Open Beauty Facts

*Get a given product.*

```python
product = openfoodfacts.openbeautyfacts.get_product(barcode)
```

*Get all products for given facets.*

Page access (pagination) is available through parameters.

```python
products = openfoodfacts.openbeautyfacts.get_by_facets({
  'packaging': 'Plastique',
  'country': 'france'
})
```

*Basic Search*

```
search_result = openfoodfacts.openbeautyfacts.products.search(query)
```

## Open Pet Food Facts

*Get a given product.*

```python
product = openfoodfacts.openpetfoodfacts.get_product(barcode)
```

*Get all products for given facets.*

Page access (pagination) is available through parameters.

```python
products = openfoodfacts.openpetfoodfacts.get_by_facets({
  'brand': 'Sans marque',
  'country': 'france'
})
```

*Basic Search*

```
search_result = openfoodfacts.openpetfoodfacts.search(query)
```

