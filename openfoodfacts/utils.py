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

def get_ocr_json_url_for_an_image(first_three_digits, second_three_digits, third_three_digits,fourth_three_digits, image_name):
    """
    Get the URL of a JSON file given a barcode in 4 chunks of 3 digits and an image name (1, 2, 3, front_fr…)
    """
	try:
		image_ocr_json = "http://world.openfoodfacts.org/images/products/" + str(first_three_digits)+ "/" + str(second_three_digits)+ "/" + str(third_three_digits)+ "/" + str(fourth_three_digits)+ "/" + str(image_name) + ".json"
		return str(image_ocr_json)
	except IndexError:
		return None
