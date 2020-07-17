Open Food Facts client for your Python applications and scripts
===============================================================

What is Open Food Facts?
------------------------

A food products database
~~~~~~~~~~~~~~~~~~~~~~~~

Open Food Facts is a database of food products with ingredients,
allergens, nutrition facts and all the tidbits of information we can
find on product labels.

Made by everyone
~~~~~~~~~~~~~~~~

Open Food Facts is a non-profit association of volunteers. 1800+
contributors like you have added 700 000+ products from 150 countries
using our Android, iPhone or Windows Phone app or their camera to scan
barcodes and upload pictures of products and their labels.

For everyone
~~~~~~~~~~~~

Data about food is of public interest and has to be open. The complete
database is published as open data and can be reused by anyone and for
any use. Check-out the cool reuses or make your own! -
https://world.openfoodfacts.org

Status
------

|Project Status| |Average time to resolve an issue| |Percentage of
issues still open| |Build Status| |codecov| |Latest Version| |License:
MIT|

Contributing
------------

Any help is welcome, as long as you don't break the continuous
integration. Fork the repository and open a Pull Request directly on the
master branch. A maintainer will review and integrate your changes.

Maintainers:

-  `Anubhav Bhargava <https://github.com/Anubhav-Bhargava>`__
-  `Frank Rousseau <https://github.com/frankrousseau>`__
-  `Pierre Slamich <https://github.com/teolemon>`__

Contributors:

-  `Agamit Sudo <https://github.com/agamitsudo>`__
-  `Daniel Stolpe <https://github.com/numberpi>`__
-  `Enioluwa Segun <https://github.com/enioluwa23>`__
-  `Nicolas Leger <https://github.com/nicolasleger>`__
-  `Pablo Hinojosa <https://github.com/Pablohn26>`__
-  `Andrea Stagi <https://github.com/astagi>`__

Copyright and License
---------------------

::

    Copyright 2016-2020 Open Food Facts

-  `License
   MIT <https://github.com/openfoodfacts/openfoodfacts-python/blob/master/LICENSE>`__

Installation
------------

::

    pip install openfoodfacts

or:

::

    git clone https://github.com/openfoodfacts/openfoodfacts-python
    cd openfoodfacts-python
    sudo python setup.py install

Docs
----

Example Usage
~~~~~~~~~~~~~

*Query a Facet*

.. code:: python

    brands = openfoodfacts.facets.get_brands()

*Basic Search*

.. code:: python

    search_result = openfoodfacts.products.search(query)

*Add a new product.*

.. code:: python

    status_code = openfoodfacts.products.add_new_product({
      'code': barcode,
      'user_id'  : myUsername,
      'password'  : myPassword,
      'product_name' : myProduct,
      'stores'  : store,
      'brands': brand,
      'packaging': packaging
    })

To see all possible capabilities, check out the `usage
guide <https://github.com/openfoodfacts/openfoodfacts-python/blob/master/docs/Usage.md>`__.

.. |Project Status| image:: https://opensource.box.com/badges/active.svg
   :target: https://opensource.box.com/badges
.. |Average time to resolve an issue| image:: https://isitmaintained.com/badge/resolution/openfoodfacts/openfoodfacts-python.svg
   :target: https://isitmaintained.com/project/openfoodfacts/openfoodfacts-python.svg
.. |Percentage of issues still open| image:: https://isitmaintained.com/badge/open/openfoodfacts/openfoodfacts-python.svg
   :target: https://isitmaintained.com/project/openfoodfacts/openfoodfacts-python.svg
.. |Build Status| image:: https://travis-ci.org/openfoodfacts/openfoodfacts-python.svg?branch=master
   :target: https://travis-ci.org/openfoodfacts/openfoodfacts-python
.. |codecov| image:: https://codecov.io/gh/openfoodfacts/openfoodfacts-python/branch/master/graph/badge.svg
   :target: https://codecov.io/gh/openfoodfacts/openfoodfacts-python
.. |Latest Version| image:: https://img.shields.io/pypi/v/openfoodfacts.svg
   :target: https://pypi.org/project/openfoodfacts
.. |License: MIT| image:: https://img.shields.io/badge/License-MIT-blue.svg
   :target: https://github.com/openfoodfacts/openfoodfacts-python/blob/master/LICENSE
