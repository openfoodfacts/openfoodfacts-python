# -*- coding: utf-8 -*-
from . import utils
import requests


def get_product(barcode, locale='world'):
    """
    Return information of a given product.
    """
    url = utils.build_url(geography=locale,
                          service='api',
                          resource_type='product',
                          parameters=barcode)
    return utils.fetch(url)


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

        url = utils.build_url(geography=locale,
                              resource_type=path,
                              parameters=str(page))
        return utils.fetch(url)['products']


def add_new_product(post_data, locale='world'):
    """
    Add a new product to OFF database.
    """
    if not post_data['code'] or not post_data['product_name']:
        raise ValueError('code or product_name not found!')

    url = utils.build_url(geography='world',
                          service='cgi',
                          resource_type='product_jqm2.pl')
    return requests.post(url, data=post_data)


def upload_image(code, imagefield, img_path):
    """
    Add new image for a product
    """
    if imagefield not in ["front", "ingredients", "nutrition"]:
        raise ValueError("Imagefield not valid!")

    image_payload = {"imgupload_%s" % imagefield: open(img_path, 'rb')}

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

    url = utils.build_url(geography=locale,
                          service='cgi',
                          resource_type='search.pl',
                          parameters=parameters)

    return utils.fetch(url, json_file=False)


def advanced_search(post_query):
    """
    Perform advanced search using OFF search engine
    """
    post_query['json'] = '1'
    url = utils.build_url(service='cgi',
                          resource_type='search.pl',
                          parameters=post_query)
    return utils.fetch(url, json_file=False)
