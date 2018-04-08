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

    def test_get_purchase_places(self):
        with requests_mock.mock() as mock:
            mock.get('https://world.openfoodfacts.org/purchase-places.json',
                     text='{"tags":["France"]}')
            res = openfoodfacts.facets.get_purchase_places()
            self.assertEquals(res, ["France"])

    def test_get_packaging_codes(self):
        with requests_mock.mock() as mock:
            mock.get('https://world.openfoodfacts.org/packager-codes.json',
                     text='{"tags":["FABRICANTE-Y-ENVASADOR"]}')
            res = openfoodfacts.facets.get_packaging_codes()
            self.assertEquals(res, ["FABRICANTE-Y-ENVASADOR"])

    def test_get_entry_dates(self):
        with requests_mock.mock() as mock:
            mock.get('https://world.openfoodfacts.org/entry-dates.json',
                     text='{"tags":["2017"]}')
            res = openfoodfacts.facets.get_entry_dates()
            self.assertEquals(res, ["2017"])

if __name__ == '__main__':
    unittest.main()
