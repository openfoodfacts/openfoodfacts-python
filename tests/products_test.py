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


if __name__ == '__main__':
    unittest.main()
