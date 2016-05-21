import json
import random
import requests
import urllib
import re

		traces = json.load(urllib.urlopen("http://world.openfoodfacts.org/traces.json"))
		ingredients = json.load(urllib.urlopen("http://world.openfoodfacts.org/ingredients.json"))
		stores = json.load(urllib.urlopen("http://world.openfoodfacts.org/stores.json"))
		packaging_codes = json.load(urllib.urlopen("http://world.openfoodfacts.org/packager-codes.json"))
		packagings = json.load(urllib.urlopen("http://world.openfoodfacts.org/packaging.json"))
		brands = json.load(urllib.urlopen("http://world.openfoodfacts.org/brands.json"))
		labels = json.load(urllib.urlopen("http://world.openfoodfacts.org/labels.json"))
		categories = json.load(urllib.urlopen("http://world.openfoodfacts.org/categories.json"))
		allergens = json.load(urllib.urlopen("http://world.openfoodfacts.org/allergens.json"))
		additives = json.load(urllib.urlopen("http://world.openfoodfacts.org/additives.json"))
		countries = json.load(urllib.urlopen("http://world.openfoodfacts.org/countries.json"))
		purchase_places = json.load(urllib.urlopen("http://world.openfoodfacts.org/purchase-places.json"))
		states = json.load(urllib.urlopen("http://world.openfoodfacts.org/states.json"))
		entry_dates = json.load(urllib.urlopen("http://world.openfoodfacts.org/entry-dates.json""))
		languages = json.load(urllib.urlopen("http://world.openfoodfacts.org/languages.json""))
		product = json.load(urllib.urlopen("http://world.openfoodfacts.org/api/v0/product/"+ str(jr['code']) +".json"))
    # http://world.openfoodfacts.org/api/v0/product/737628064502.json



