# Open Food Facts client for your Python applications and scripts

<div align="center">
  <img width="178" src="https://static.openfoodfacts.org/images/misc/openfoodfacts-logo-en-178x150.png" alt="Open Food Facts"/>
</div>

## What is Open Food Facts?

### A food products database

Open Food Facts is a database of food products with ingredients, allergens, nutrition facts and all the tidbits of information we can find on product labels.

### Made by everyone

Open Food Facts is a non-profit association of volunteers.
1800+ contributors like you have added 700 000+ products from 150 countries using our Android, iPhone or Windows Phone app or their camera to scan barcodes and upload pictures of products and their labels.

### For everyone

Data about food is of public interest and has to be open. The complete database is published as open data and can be reused by anyone and for any use. Check-out the cool reuses or make your own!
- <https://world.openfoodfacts.org>

## Status

[![Project Status](https://opensource.box.com/badges/active.svg)](https://opensource.box.com/badges)
[![Average time to resolve an issue](https://isitmaintained.com/badge/resolution/openfoodfacts/openfoodfacts-python.svg)](https://isitmaintained.com/project/openfoodfacts/openfoodfacts-python.svg "Average time to resolve an issue")
[![Percentage of issues still open](https://isitmaintained.com/badge/open/openfoodfacts/openfoodfacts-python.svg)](https://isitmaintained.com/project/openfoodfacts/openfoodfacts-python.svg "Percentage of issues still open")
[![Build Status](https://travis-ci.org/openfoodfacts/openfoodfacts-python.svg?branch=master)](https://travis-ci.org/openfoodfacts/openfoodfacts-python)
[![codecov](https://codecov.io/gh/openfoodfacts/openfoodfacts-python/branch/master/graph/badge.svg)](https://codecov.io/gh/openfoodfacts/openfoodfacts-python)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://github.com/openfoodfacts/openfoodfacts-python/blob/master/LICENSE)

## Contributing

Any help is welcome, as long as you don't break the continuous integration.
Fork the repository and open a Pull Request directly on the master branch.
A maintainer will review and integrate your changes.

Maintainers:

- [Anubhav Bhargava](https://github.com/Anubhav-Bhargava)
- [Frank Rousseau](https://github.com/frankrousseau)
- [Pierre Slamich](https://github.com/teolemon)

Contributors:

- [Agamit Sudo](https://github.com/agamitsudo)
- [Daniel Stolpe](https://github.com/numberpi)
- [Enioluwa Segun](https://github.com/enioluwa23)
- [Nicolas Leger](https://github.com/nicolasleger)
- [Pablo Hinojosa](https://github.com/Pablohn26)

## Copyright and License

    Copyright 2016-2019 Open Food Facts

- [License](./LICENSE)

## Installation

    sudo pip install git+https://github.com/openfoodfacts/openfoodfacts-python

or:

    git clone https://github.com/openfoodfacts/openfoodfacts-python
    cd openfoodfacts-python
    sudo python setup.py install

## Docs

### Example Usage

*Query a Facet*

```python
brands = openfoodfacts.facets.get_brands()
```

*Basic Search*

```python
search_result = openfoodfacts.products.search(query)
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

To see all possible capabilities, check out the [usage guide](./docs/Usage.md).
