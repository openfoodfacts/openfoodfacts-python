import unittest
import os
import openfoodfacts
import requests
import requests_mock


class TestProducts(unittest.TestCase):

    def test_get_product(self):
        with requests_mock.mock() as mock:
            mock.get(
                'https://world.openfoodfacts.org/api/v0/product/1223435.json',
                text='{"name":"product_test"}')
            res = openfoodfacts.get_product('1223435')
            self.assertEqual(res, {'name': 'product_test'})

    def test_get_by_trace(self):
        with requests_mock.mock() as mock:
            mock.get('https://world.openfoodfacts.org/trace/egg/1.json',
                     text='{"products":["omelet"]}')
            res = openfoodfacts.products.get_by_trace('egg')
            self.assertEqual(res, ["omelet"])

    def test_get_by_trace_pagination(self):
        with requests_mock.mock() as mock:
            mock.get('https://world.openfoodfacts.org/trace/egg/2.json',
                     text='{"products":["omelet"]}')
            res = openfoodfacts.products.get_by_trace('egg', 2)
            self.assertEqual(res, ["omelet"])

    def test_get_by_country(self):
        with requests_mock.mock() as mock:
            mock.get('https://world.openfoodfacts.org/country/france/1.json',
                     text='{"products":["omelet"]}')
            res = openfoodfacts.products.get_by_country('france')
            self.assertEqual(res, ["omelet"])

    def test_get_by_country_and_trace(self):
        res = openfoodfacts.products.get_by_facets({})
        self.assertEqual(res, [])

        with requests_mock.mock() as mock:
            mock.get(
                'https://world.openfoodfacts.org/country/'
                'france/trace/egg/1.json',
                text='{"products":["omelet"]}')
            res = openfoodfacts.products.get_by_facets(
                    {'trace': 'egg', 'country': 'france'})
            self.assertEqual(res, ["omelet"])

    def test_search(self):
        with requests_mock.mock() as mock:
            mock.get(
                'https://world.openfoodfacts.org/cgi/search.pl?' +
                'search_terms=kinder bueno&json=1&page=' +
                '1&page_size=20&sort_by=unique_scans',
                text='{"products":["kinder bueno"], "count": 1}')
            res = openfoodfacts.products.search('kinder bueno')
            self.assertEqual(res["products"],  ["kinder bueno"])
            mock.get(
                'https://world.openfoodfacts.org/cgi/search.pl?' +
                'search_terms=banania&json=1&page=' +
                '2&page_size=10&sort_by=unique_scans',
                text='{"products":["banania", "banania big"], "count": 2}')
            res = openfoodfacts.products.search(
                'banania', page=2, page_size=10)
            self.assertEqual(res["products"],  ["banania", "banania big"])

    def test_advanced_search(self):
        with requests_mock.mock() as mock:
            mock.get(
                'https://world.openfoodfacts.org/cgi/search.pl?' +
                'search_terms=coke&tagtype_0=packaging&' +
                'tag_contains_0=contains&tag_0=plastic&' +
                'nutriment_0=energy&nutriment_compare_0=gt&' +
                'nutriment_value_0=0&sort_by=unique_scans&' +
                'page_size=20',
                text= '{"products":["Diet Coke"], "count": 1}')
            res = openfoodfacts.products.advanced_search({
                  "search_terms":"coke",
                  "tagtype_0":"packaging",
                  "tag_contains_0":"contains",
                  "tag_0":"plastic",
                  "nutriment_0":"energy",
                  "nutriment_compare_0":"gt",
                  "nutriment_value_0":"0",
                  "sort_by":"unique_scans",
                  "page_size":"20"
                })
            self.assertEqual(res["products"],["Diet Coke"])

if __name__ == '__main__':
    unittest.main()
