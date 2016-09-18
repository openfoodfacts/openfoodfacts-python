# -*- coding: utf-8 -*-
import utils


SEARCH_PATH = "cgi/search.pl"


def get_product(barcode):
    """
    Return information of a given product.
    """
    return utils.fetch('api/v0/product/%s' % barcode)


def search(query, pagination=20):
    """
    Perform a search using Open Food Facts search engine.
    """
    pass
