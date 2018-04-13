# -*- coding: utf-8 -*-
import requests
from . import utils


def get_product(barcode, locale='world'):
    """
    Return information of a given product.
    """
    return utils.fetch(utils.build_url(geography=locale,
                                       service='api',
                                       resource_type='product',
                                       parameters=barcode,
                                       entity="pet"))


def get_by_facets(query, page=1, locale='world'):
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

        return utils. \
            fetch(utils.build_url(geography=locale,
                                  resource_type=path,
                                  parameters=str(page),
                                  entity="pet"))['products']


def search(query, page=1, page_size=20,
           sort_by='unique_scans', locale='world'):
    """
    Perform a search using Open Pet Food Facts search engine.
    """
    parameters = {'search_terms': query,
                  'page': page,
                  'page_size': page_size,
                  'sort_by': sort_by,
                  'json': '1'}

    path = utils.build_url(geography=locale,
                           service='cgi',
                           resource_type='search.pl',
                           parameters=parameters,
                           entity="pet")

    return utils.fetch(path, json_file=False)
