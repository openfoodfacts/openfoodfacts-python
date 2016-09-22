import requests

API_URL = "http://world.openfoodfacts.org/"


def fetch(path):
    """
    Fetch data at a given path assuming that target match a json file and is
    located on the OFF API.
    """
    response = requests.get("%s%s.json" % (API_URL, path))
    return response.json()
