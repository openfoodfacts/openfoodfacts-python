# Open Food Facts client for your python scripts


### install

    sudo pip install git+https://github.com/openfoodfacts/openfoodfacts-python

or:

    git clone https://github.com/openfoodfacts/openfoodfacts-python
    cd openfoodfacts
    sudo python setup.py install


### Docs

#### Facets

*Get all available additives.*

```python
traces = openfoodfacts.get_additives()
```

*Get all available allergens.*

```python
allergens = openfoodfacts.get_allergens()
```

*Get all available brands.*

```python
brands = openfoodfacts.get_brands()
```

*Get all available categories.*

```python
categories = openfoodfacts.get_categories()
```

*Get all available countries.*

```python
countries = openfoodfacts.get_countries()
```

*Get all available entry dates.*

```python
entry_dates = openfoodfacts.get_entry_dates()
```

*Get all available ingredients.*

```python
ingredients = openfoodfacts.get_ingredients()
```

*Get all available languages.*

```python
languages = openfoodfacts.get_languages()
```

*Get all available packagings.*

```python
packagings = openfoodfacts.get_packagings()
```

*Get all available packaging codes.*

```python
codes = openfoodfacts.get_packaging_codes()
```

*Get all available purchase places.*

```python
places = openfoodfacts.get_purchase_places()
```

*Get all available stores.*

```python
stores = openfoodfacts.get_stores()
```

*Get all available trace types.*

```python
traces = openfoodfacts.get_traces()
```

*Get all available states.*

```python
states = openfoodfacts.get_states()
```


#### Product

*Get a given product.*

```python
product = openfoodfacts.get_product(barcode)
```
