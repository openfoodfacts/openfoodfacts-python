# -*- coding: utf-8 -*-
from . import utils


SEARCH_PATH = "cgi/search.pl"


def get_product(barcode):
    """
    Return information of a given product.
    """
    return utils.fetch('api/v0/product/%s' % barcode)


def get_by_facets(query):
    """
    Return products for a set of facets.
    """
    path = []
    keys = query.keys()
    keys.sort()
    for key in keys:
        path.append(key)
        path.append(query[key])

    return utils.fetch('/'.join(path))['products']


def search(query, pagination=20):
    """
    Perform a search using Open Food Facts search engine.
    """
    pass
