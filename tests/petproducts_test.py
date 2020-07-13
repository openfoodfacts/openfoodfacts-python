import unittest
import os
import openfoodfacts
import requests
import requests_mock


class TestPetProducts(unittest.TestCase):

    def test_get_product(self):
        with requests_mock.mock() as mock:
            mock.get(
                'https://world.openpetfoodfacts.org/api/v0/product/1223435.json',
                text='{"name":"product_test"}')
            res = openfoodfacts.pet_products.get_product('1223435')
            self.assertEqual(res, {'name': 'product_test'})

    def test_get_by_country_and_trace(self):
        res = openfoodfacts.pet_products.get_by_facets({})
        self.assertEqual(res, [])

        with requests_mock.mock() as mock:
            mock.get(
                'https://world.openpetfoodfacts.org/brand/'
                'Sans%20marque/country/france/1.json',
                text='{"products":["croquants"]}')
            res = openfoodfacts.pet_products.get_by_facets(
                    {'brand': 'Sans marque', 'country': 'france'})
            self.assertEqual(res, ["croquants"])

    def test_get_by_country_and_trace_all(self):
        with requests_mock.mock() as mock:
            mock.get(
                'https://world.openpetfoodfacts.org/brand/'
                'Sans%20marque/country/france/1.json',
                text='{"products":["croquants"], "count": 1}')
            mock.get(
                'https://world.openpetfoodfacts.org/brand/'
                'Sans%20marque/country/france/2.json',
                text='{"products":["croquants small", "croquants big"], "count": 2}')
            mock.get(
                'https://world.openpetfoodfacts.org/brand/'
                'Sans%20marque/country/france/3.json',
                text='{"products":[], "count": 0}')
            res = openfoodfacts.pet_products.get_all_by_facets(
                    {'brand': 'Sans marque', 'country': 'france'})
            expected_products_sequence = ["croquants", "croquants small", "croquants big"]
            for i, product in enumerate(res):
                self.assertEqual(product, expected_products_sequence[i])

    def test_search(self):
        with requests_mock.mock() as mock:
            mock.get(
                'https://world.openpetfoodfacts.org/cgi/search.pl?' +
                'search_terms=le chat&json=1&page=' +
                '1&page_size=20&sort_by=unique_scans',
                text='{"products":["le chat"], "count": 1}')
            res = openfoodfacts.pet_products.search('le chat')
            self.assertEqual(res['products'],  ["le chat"])
            mock.get(
                'https://world.openpetfoodfacts.org/cgi/search.pl?' +
                'search_terms=croquants&json=1&page=' +
                '2&page_size=10&sort_by=unique_scans',
                text='{"products":["croquants", "croquants big"], "count": 2}')
            res = openfoodfacts.pet_products.search('croquants', page=2, page_size=10)
            self.assertEqual(res['products'],  ["croquants", "croquants big"])

    def test_search_all(self):
        with requests_mock.mock() as mock:
            mock.get(
                'https://world.openpetfoodfacts.org/cgi/search.pl?' +
                'search_terms=croquants&json=1&page=' +
                '1&page_size=20&sort_by=unique_scans',
                text='{"products":["croquants small"], "count": 1}')
            mock.get(
                'https://world.openpetfoodfacts.org/cgi/search.pl?' +
                'search_terms=croquants&json=1&page=' +
                '2&page_size=20&sort_by=unique_scans',
                text='{"products":["croquants", "croquants big"], "count": 2}')
            mock.get(
                'https://world.openpetfoodfacts.org/cgi/search.pl?' +
                'search_terms=croquants&json=1&page=' +
                '3&page_size=20&sort_by=unique_scans',
                text='{"products":[], "count": 2}')
            res = openfoodfacts.pet_products.search_all('croquants')
            expected_products_sequence = ["croquants small", "croquants", "croquants big"]
            for i, product in enumerate(res):
                self.assertEqual(product, expected_products_sequence[i])


if __name__ == '__main__':
    unittest.main()
