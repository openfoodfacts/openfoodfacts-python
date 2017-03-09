import unittest
import openfoodfacts
import requests_mock


class TestFacets(unittest.TestCase):

    def test_get_traces(self):
        with requests_mock.mock() as mock:
            mock.get('https://world.openfoodfacts.org/traces.json',
                     text='{"tags":["egg"]}')
            res = openfoodfacts.facets.get_traces()
            self.assertEquals(res, ["egg"])

    def test_get_additives(self):
        with requests_mock.mock() as mock:
            mock.get('https://world.openfoodfacts.org/additives.json',
                     text='{"tags":["additive"]}')
            res = openfoodfacts.facets.get_additives()
            self.assertEquals(res, ["additive"])


if __name__ == '__main__':
    unittest.main()
