# -*- coding: utf-8 -*-
from . import utils
import re


SEARCH_PATH = "cgi/search.pl"


def get_product(barcode):
    """
    Return information of a given product.
    """
    return utils.fetch('api/v0/product/%s' % barcode)


def get_user_products:
    """
    Return all the products added or edited by the user.
    """
    
    #Login
    c = utils.login_into_OFF()
    r = c.get(utils.API_URL)
    
    complete_html = r.text
    
    #find the username
    for single_line in complete_html.splitlines():
        if "You are connected as" in single_line:
            name=single_line.split()[4][:-4]
    
    #go to homepage of user
    url = utils.API_URL + "contributor/" + name
    r = c.post(url)
    
    #get all the products added or edited by the user
	products = []
    for single_line in r.text.splitlines():
        if "/product/" in single_line:
            products.append(get_product(single_line.split("=")[2][1:-2]))
        
    #return list of user products
    return products


def get_by_facets(query, page=1):
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

        return utils.fetch('%s/%s' % ('/'.join(path), page))['products']


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
