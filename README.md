# Open Food Facts Python SDK

<div align="center">
  <img width="400" src="https://blog.openfoodfacts.org/wp-content/uploads/2022/05/EXE_LOGO_OFF_RVB_Plan-de-travail-1-copie-0-1-768x256.jpg" alt="Open Food Facts"/>
</div>

## Status

[![Project Status](https://opensource.box.com/badges/active.svg)](https://opensource.box.com/badges)
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

The easiest way to install the SDK is through pip:

    pip install openfoodfacts

or manually from source:

    git clone https://github.com/openfoodfacts/openfoodfacts-python
    cd openfoodfacts-python
    python setup.py install

## Examples

*Get information about a product*

```python
code = "3017620422003"
api.product.get(code)
```

*Perform text search*

```python
results = api.product.text_search("mineral water")
```

*Create a new product or update an existing one*

```python
results = api.product.update(CODE, body)
```

with `CODE` the product barcode and `body` the update body.

To see all possible capabilities, check out the [usage guide](https://openfoodfacts.github.io/openfoodfacts-python/usage/).

## Third party applications
If you use this SDK, feel free to open a PR to add your application in this list.
