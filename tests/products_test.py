import unittest
import os
import openfoodfacts
import requests
import requests_mock


class TestProducts(unittest.TestCase):

    def test_get_product(self):
        with requests_mock.mock() as mock:
            mock.get(
                'http://world.openfoodfacts.org/api/v0/product/1223435.json',
                text='{"name":"product_test"}')
            res = openfoodfacts.get_product('1223435')
            self.assertEquals(res, {'name': 'product_test'})

    def test_get_by_trace(self):
        with requests_mock.mock() as mock:
            mock.get('http://world.openfoodfacts.org/trace/egg.json',
                     text='{"products":["omelet"]}')
            res = openfoodfacts.products.get_by_trace('egg')
            self.assertEquals(res, ["omelet"])

    def test_get_by_country(self):
        with requests_mock.mock() as mock:
            mock.get('http://world.openfoodfacts.org/country/france.json',
                     text='{"products":["omelet"]}')
            res = openfoodfacts.products.get_by_country('france')
            self.assertEquals(res, ["omelet"])

    def test_get_by_country_and_trace(self):
        res = openfoodfacts.products.get_by_facets({})
        self.assertEquals(res, [])

        with requests_mock.mock() as mock:
            mock.get(
                'http://world.openfoodfacts.org/country/france/trace/egg.json',
                text='{"products":["omelet"]}')
            res = openfoodfacts.products.get_by_facets(
                    {'trace': 'egg', 'country': 'france'})
            self.assertEquals(res, ["omelet"])

    def test_search(self):
        with requests_mock.mock() as mock:
            mock.get(
                'http://world.openfoodfacts.org/cgi/search.pl?' +
                'search_terms=kinder bueno&json=1&page=' +
                '1&page_size=20&sort_by=unique_scans',
                text='{"products":["kinder bueno"], "count": 1}')
            res = openfoodfacts.products.search('kinder bueno')
            self.assertEquals(res["products"],  ["kinder bueno"])
            mock.get(
                'http://world.openfoodfacts.org/cgi/search.pl?' +
                'search_terms=banania&json=1&page=' +
                '2&page_size=10&sort_by=unique_scans',
                text='{"products":["banania", "banania big"], "count": 2}')
            res = openfoodfacts.products.search(
                'banania', page=2, page_size=10)
            self.assertEquals(res["products"],  ["banania", "banania big"])

if __name__ == '__main__':
    unittest.main()
