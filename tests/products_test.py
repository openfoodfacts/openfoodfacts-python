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

    def test_get_by_trace(self):
        with requests_mock.mock() as mock:
            mock.get('http://world.openfoodfacts.org/country/france.json',
                     text='{"products":["omelet"]}')
            res = openfoodfacts.products.get_by_country('france')
            self.assertEquals(res, ["omelet"])


if __name__ == '__main__':
    unittest.main()
