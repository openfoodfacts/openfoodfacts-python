# -*- coding: utf-8 -*-
from . import utils
import requests
import urllib


def get_product(barcode, locale='world'):
    """
    Return information of a given product.
    """
    return utils.fetch(utils.build_url(geography=locale,
                                       service='api',
                                       resource_type='product',
                                       parameters=barcode))


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
                                  parameters=str(page)))['products']


def add_new_product(postData, locale='world'):
    """
    Add a new product to OFF database.
    """
    if not postData['code'] or not postData['product_name']:
        raise ValueError('code or product_name not found!')

    return requests.post(utils.build_url(geography='world',
                                         service='cgi',
                                         resource_type='product_jqm2.pl'),
                         data=postData)


def upload_image(code, imagefield, img_path):
    """
    Add new image for a product
    """
    if imagefield == 'front':
        image_payload = {"imgupload_front": open(img_path, 'rb')}

    elif imagefield == 'ingredients':
        image_payload = {"imgupload_ingredients": open(img_path, 'rb')}

    elif imagefield == 'nutrition':
        image_payload = {"imgupload_nutrition": open(img_path, 'rb')}

    else:
        raise ValueError("Imagefield not valid!")

    url = utils.build_url(service='cgi',
                          resource_type='product_image_upload.pl')

    other_payload = {'code': code, 'imagefield': imagefield}

    headers = {'Content-Type': 'multipart/form-data'}

    return requests.post(url=url,
                         data=other_payload,
                         files=image_payload,
                         headers=headers)


def search(query, page=1, page_size=20,
           sort_by='unique_scans', locale='world'):
    """
    Perform a search using Open Food Facts search engine.
    """
    parameters = {'search_terms': query,
                  'page': page,
                  'page_size': page_size,
                  'sort_by': sort_by,
                  'json': '1'}

    path = utils.build_url(geography=locale,
                           service='cgi',
                           resource_type='search.pl',
                           parameters=parameters)

    return utils.fetch(path, json_file=False)


def advanced_search(postQuery):
    """
    Perform advanced search using OFF search engine
    """
    postQuery['json'] = '1'
    path = utils.build_url(service='cgi',
                           resource_type='search.pl',
                           parameters=postQuery)
    return utils.fetch(path, json_file=False)
