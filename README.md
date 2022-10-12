# Open Food Facts Python SDK

<div align="center">
  <img width="400" src="https://blog.openfoodfacts.org/wp-content/uploads/2022/05/EXE_LOGO_OFF_RVB_Plan-de-travail-1-copie-0-1-768x256.jpg" alt="Open Food Facts"/>
</div>

## What is Open Food Facts?

### A food products database

Open Food Facts is a database of food products with ingredients, allergens, nutrition facts and all the tidbits of information we can find on product labels.

### Made by everyone

Open Food Facts is a non-profit association of volunteers.
25000+ contributors like you have added 2.5 million+ products from 150 countries using our Android, iPhone or Windows Phone app or their camera to scan barcodes and upload pictures of products and their labels.

### For everyone

Data about food is of public interest and has to be open. The complete database is published as open data and can be reused by anyone and for any use. Check-out the cool reuses or make your own! 

The Open Food Facts Website: <https://world.openfoodfacts.org>

## Status

[![Project Status](https://opensource.box.com/badges/active.svg)](https://opensource.box.com/badges)
[![Average time to resolve an issue](https://isitmaintained.com/badge/resolution/openfoodfacts/openfoodfacts-python.svg)](https://isitmaintained.com/project/openfoodfacts/openfoodfacts-python.svg "Average time to resolve an issue")
[![Percentage of issues still open](https://isitmaintained.com/badge/open/openfoodfacts/openfoodfacts-python.svg)](https://isitmaintained.com/project/openfoodfacts/openfoodfacts-python.svg "Percentage of issues still open")
[![Build Status](https://travis-ci.org/openfoodfacts/openfoodfacts-python.svg?branch=master)](https://travis-ci.org/openfoodfacts/openfoodfacts-python)
[![codecov](https://codecov.io/gh/openfoodfacts/openfoodfacts-python/branch/master/graph/badge.svg)](https://codecov.io/gh/openfoodfacts/openfoodfacts-python)
[![Latest Version](https://img.shields.io/pypi/v/openfoodfacts.svg)](https://pypi.org/project/openfoodfacts)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://github.com/openfoodfacts/openfoodfacts-python/blob/master/LICENSE)

## Contributing

Any help is welcome, as long as you don't break the continuous integration.
Fork the repository and open a Pull Request directly on the "develop" branch.
A maintainer will review and integrate your changes.

Maintainers:

- [Anubhav Bhargava](https://github.com/Anubhav-Bhargava)
- [Frank Rousseau](https://github.com/frankrousseau)
- [Pierre Slamich](https://github.com/teolemon)

Contributors:

- Agamit Sudo
- [Daniel Stolpe](https://github.com/numberpi)
- [Enioluwa Segun](https://github.com/enioluwas)
- [Nicolas Leger](https://github.com/nicolasleger)
- [Pablo Hinojosa](https://github.com/Pablohn26)
- [Andrea Stagi](https://github.com/astagi)
- [Benoît Prieur](https://github.com/benprieur)
- [Aadarsh A](https://github.com/aadarsh-ram)

## Copyright and License

    Copyright 2016-2022 Open Food Facts

The Open Food Facts Python SDK is licensed under the [MIT License](https://github.com/openfoodfacts/openfoodfacts-python/blob/develop/LICENSE).

## Installation

    pip install openfoodfacts

or:

    git clone https://github.com/openfoodfacts/openfoodfacts-python
    cd openfoodfacts-python
    sudo python setup.py install

## Examples

- *Query a facet*

```python
brands = openfoodfacts.facets.get_brands()
```

- *Basic search*

```python
search_result = openfoodfacts.products.search(query)
```

- *Add a new product*

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

To see all possible capabilities, check out the [usage guide](https://openfoodfacts.github.io/openfoodfacts-python/Usage/).

## Third party applications
If you use this SDK, feel free to open a PR to add your application in this list.
