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

    if len(keys) == 0:
        return []

    else:
        keys = sorted(keys)
        for key in keys:
            path.append(key)
            path.append(query[key])

        return utils.fetch('/'.join(path))['products']


def search(query, page=1, page_size=20, sort_by='unique_scans'):
    """
    Perform a search using Open Food Facts search engine.
    """
    path = "cgi/search.pl?search_terms={query}&json=1&" + \
           "page={page}&page_size={page_size}&sort_by={sort_by}"
    path = path.format(
        query=query,
        page=page,
        page_size=page_size,
        sort_by=sort_by
    )
    return utils.fetch(path, json_file=False)
