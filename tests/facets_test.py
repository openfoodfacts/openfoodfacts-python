import unittest
import os
import openfoodfacts
import requests
import requests_mock


class TestFacets(unittest.TestCase):

    def test_get_traces(self):
        with requests_mock.mock() as mock:
            mock.get('http://world.openfoodfacts.org/traces.json',
                     text='{"tags":["egg"]}')
            res = openfoodfacts.get_traces()
            self.assertEquals(res, ["egg"])

    def test_get_additives(self):
        with requests_mock.mock() as mock:
            mock.get('http://world.openfoodfacts.org/additives.json',
                     text='{"tags":["additive"]}')
            res = openfoodfacts.get_additives()
            self.assertEquals(res, ["additive"])


if __name__ == '__main__':
    unittest.main()
