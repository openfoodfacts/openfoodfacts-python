import unittest
import os
import openfoodfacts
import requests
import requests_mock


class TestBeautyProducts(unittest.TestCase):

    def test_get_product(self):
        with requests_mock.mock() as mock:
            mock.get(
                'https://world.openbeautyfacts.org/api/v0/product/1223435.json',
                text='{"name":"product_beauty_test"}')
            res = openfoodfacts.beauty_products.get_product('1223435')
            self.assertEqual(res, {'name': 'product_beauty_test'})

    def test_get_by_country_and_trace(self):
        res = openfoodfacts.beauty_products.get_by_facets({})
        self.assertEqual(res, [])

        with requests_mock.mock() as mock:
            mock.get(
                'https://world.openbeautyfacts.org/country/'
                'france/packaging/plastique/1.json',
                text='{"products":["parfum"]}')
            res = openfoodfacts.beauty_products.get_by_facets(
                    {'packaging': 'Plastique', 'country': 'france'})
            self.assertEqual(res, ["parfum"])

    def test_get_by_country_and_trace_all(self):
        with requests_mock.mock() as mock:
            mock.get(
                'https://world.openbeautyfacts.org/brand/'
                'Sans%20marque/country/france/1.json',
                text='{"products":["parfum"], "count": 1}')
            mock.get(
                'https://world.openbeautyfacts.org/brand/'
                'Sans%20marque/country/france/2.json',
                text='{"products":["parfum small", "parfum big"], "count": 2}')
            mock.get(
                'https://world.openbeautyfacts.org/brand/'
                'Sans%20marque/country/france/3.json',
                text='{"products":[], "count": 0}')
            res = openfoodfacts.beauty_products.get_all_by_facets(
                    {'brand': 'Sans marque', 'country': 'france'})
            expected_products_sequence = ["parfum", "parfum small", "parfum big"]
            for i, product in enumerate(res):
                self.assertEqual(product, expected_products_sequence[i])

    def test_search(self):
        with requests_mock.mock() as mock:
            mock.get(
                'https://world.openbeautyfacts.org/cgi/search.pl?' +
                'search_terms=deo axe&json=1&page=' +
                '1&page_size=20&sort_by=unique_scans',
                text='{"products":["deo axe"], "count": 1}')
            res = openfoodfacts.beauty_products.search('deo axe')
            self.assertEqual(res['products'],  ["deo axe"])
            mock.get(
                'https://world.openbeautyfacts.org/cgi/search.pl?' +
                'search_terms=deo axe&json=1&page=' +
                '2&page_size=10&sort_by=unique_scans',
                text='{"products":["deo axe", "deo axe big"], "count": 2}')
            res = openfoodfacts.beauty_products.search('deo axe', page=2, page_size=10)
            self.assertEqual(res['products'],  ["deo axe", "deo axe big"])

    def test_search_all(self):
        with requests_mock.mock() as mock:
            mock.get(
                'https://world.openbeautyfacts.org/cgi/search.pl?' +
                'search_terms=deo axe&json=1&page=' +
                '1&page_size=20&sort_by=unique_scans',
                text='{"products":["deo axe small"], "count": 1}')
            mock.get(
                'https://world.openbeautyfacts.org/cgi/search.pl?' +
                'search_terms=deo axe&json=1&page=' +
                '2&page_size=20&sort_by=unique_scans',
                text='{"products":["deo axe", "deo axe big"], "count": 2}')
            mock.get(
                'https://world.openbeautyfacts.org/cgi/search.pl?' +
                'search_terms=deo axe&json=1&page=' +
                '3&page_size=20&sort_by=unique_scans',
                text='{"products":[], "count": 2}')
            res = openfoodfacts.beauty_products.search_all('deo axe')
            expected_products_sequence = ["deo axe small", "deo axe", "deo axe big"]
            for i, product in enumerate(res):
                self.assertEqual(product, expected_products_sequence[i])


if __name__ == '__main__':
    unittest.main()
