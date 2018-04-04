# -*- coding: utf-8 -*-
from . import utils
import requests
import urllib


SEARCH_PATH = "cgi/search.pl?"


def get_product(barcode, locale='world'):
    """
    Return information of a given product.
    """
    return utils.fetch('api/v0/product/%s' % barcode, locale)


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
            fetch('%s/%s' % ('/'.join(path), page), locale)['products']


def add_new_product(postData, locale='world'):
    """
    Add a new product to OFF database.
    """
    if not postData['code'] or not postData['product_name']:
        raise ValueError('code or product_name not found!')

    return requests. \
        post(utils.API_URL % (locale)+"cgi/product_jqm2.pl", data=postData)


def upload_image(code, imagefield, path):
    """
    Add new image for a product
    """
    if imagefield == 'front':
        image_payload = {"imgupload_front": open(path, 'rb')}

    elif imagefield == 'ingredients':
        image_payload = {"imgupload_ingredients": open(path, 'rb')}

    elif imagefield == 'nutrition':
        image_payload = {"imgupload_nutrition": open(path, 'rb')}

    else:
        raise ValueError("Imagefield not valid!")

    url = "https://world.openfoodfacts.org/cgi/product_image_upload.pl"

    other_payload = {'code': code, 'imagefield': imagefield}

    headers = {'Content-Type': 'multipart/form-data'}

    request_content = requests.post(url=url,
                                    data=other_payload,
                                    files=image_payload,
                                    headers=headers)

    return request_content


def search(query, page=1, page_size=20,
           sort_by='unique_scans', locale='world'):
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
    return utils.fetch(path, locale, json_file=False)


def advanced_search(postQuery):
    """
    Perform advanced search using OFF search engine
    """
    path = SEARCH_PATH + urllib.urlencode(postQuery) + "&json=1"
    return utils.fetch(path, json_file=False)
