import requests

API_URL = "http://world.openfoodfacts.org/"


def fetch(path, json_file=True):
    """
    Fetch data at a given path assuming that target match a json file and is
    located on the OFF API.
    """
    if json_file:
        path = "%s%s.json" % (API_URL, path)
    else:
        path = "%s%s" % (API_URL, path)

    response = requests.get(path)
    return response.json()
