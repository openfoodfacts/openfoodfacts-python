# Open Food Facts client for your Python applications and scripts

<div align="center">
  <img width="178" src="https://static.openfoodfacts.org/images/misc/openfoodfacts-logo-en-178x150.png" alt="Open Food Facts"/>
</div>

## What is Open Food Facts?
### A food products database

Open Food Facts is a database of food products with ingredients, allergens, nutrition facts and all the tidbits of information we can find on product labels. 

### Made by everyone

Open Food Facts is a non-profit association of volunteers.
1800+ contributors like you have added 43 000+ products from 150 countries using our Android, iPhone or Windows Phone app or their camera to scan barcodes and upload pictures of products and their labels.

### For everyone

Data about food is of public interest and has to be open. The complete database is published as open data and can be reused by anyone and for any use. Check-out the cool reuses or make your own!
- <https://world.openfoodfacts.org>

**Status**
===

[![Project Status](http://opensource.box.com/badges/active.svg)](http://opensource.box.com/badges)
[![Average time to resolve an issue](http://isitmaintained.com/badge/resolution/openfoodfacts/openfoodfacts-python.svg)](http://isitmaintained.com/project/openfoodfacts/openfoodfacts-python.svg "Average time to resolve an issue")
[![Percentage of issues still open](http://isitmaintained.com/badge/open/openfoodfacts/openfoodfacts-python.svg)](http://isitmaintained.com/project/openfoodfacts/openfoodfacts-python.svg "Percentage of issues still open")

## Contributing

The project is initially started by [](https://github.com/), other contributors include:
- [Pierre Slamich](https://github.com/teolemon)

## Copyright and License

    Copyright 2016 Open Food Facts


### Installation

    sudo pip install git+https://github.com/openfoodfacts/openfoodfacts-python

or:

    git clone https://github.com/openfoodfacts/openfoodfacts-python
    cd openfoodfacts-python
    sudo python setup.py install


### Docs

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

#### Products by facet

*Get all products for given facets.*

Page access (pagination) is available through parameters.

```python
products = openfoodfacts.products.get_by_facets({
  'trace': 'egg',
  'country': 'france',
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

```
status_code = openfoodfacts.products.add_new_product({
  'code': barcode,
  'user_id'  : myUsername,
  'password'  : myPassword,
  'product_name' : myProduct,
  'stores'  : store,
  'brands': brand,
  'packaging': packaging,
})
```

*Upload an image.*

```
status_code = openfoodfacts.products.upload_image(barcode, imagefield, img_path)
```

#### Search

*Basic Search*

```
search_result = openfoodfacts.products.search(query)
```

*Advanced Search*

Can pass in any [parameters](https://en.wiki.openfoodfacts.org/API/Read/Search#Parameters).
```
search_result=openfoodfacts.products.advanced_search({
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

#### Open Beauty Facts

*Get a given product.*

```python
product = openfoodfacts.openbeautyfacts.get_product(barcode)
```

*Get all products for given facets.*

Page access (pagination) is available through parameters.

```python
products = openfoodfacts.openbeautyfacts.get_by_facets({
  'packaging': 'Plastique',
  'country': 'france',
})
```

*Basic Search*

```
search_result = openfoodfacts.openbeautyfacts.products.search(query)
```

#### Open Pet Food Facts

*Get a given product.*

```python
product = openfoodfacts.openpetfoodfacts.get_product(barcode)
```

*Get all products for given facets.*

Page access (pagination) is available through parameters.

```python
products = openpetfoodfacts.get_by_facets({
  'brand': 'Sans marque',
  'country': 'france',
})
```

*Basic Search*

```
search_result = openfoodfacts.openpetfoodfacts.search(query)
```

