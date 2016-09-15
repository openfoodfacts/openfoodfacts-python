import requests

API_URL = "http://world.openfoodfacts.org/"


"""
Fetch data at a given path assuming that target match a json file and is
located on the OFF API.
"""
def fetch(path):
    print "%s%s.json" % (API_URL, path)
    response = requests.get("%s%s.json" % (API_URL, path))
    return response.json()
