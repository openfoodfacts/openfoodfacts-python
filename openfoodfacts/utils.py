import requests
import re
import getpass

API_URL = "https://world.openfoodfacts.org/"


def login_into_OFF():
	
	#Get username and pasword
	username = raw_input('Username:')
	pswd = getpass.getpass('Password:')

	payload = {'user_id': username, 'password': pswd}

	#create a requests session
	with requests.Session() as c:
		#post the username and password on the website
		r = c.post(API_URL, data=payload)

		#get the complete html text
		complete_html = r.text

		#check if login is successfull
		if re.search('You are connected as', complete_html):
			print "Login Successfull"

		else:
			print "Incorrect username or password"
			exit()

		#Return the session object
		return c
	

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


def get_ocr_json_url_for_an_image(first_three_digits,
                                  second_three_digits,
                                  third_three_digits,
                                  fourth_three_digits,
                                  image_name):
    """
    Get the URL of a JSON file given a barcode in 4 chunks of 3 digits and an
    image name (1, 2, 3, front_fr...).
    """
    url = "https://world.openfoodfacts.org/images/products/"
    url += "%s/%s/%s/%s/%s.json" % (
        first_three_digits,
        second_three_digits,
        third_three_digits,
        fourth_three_digits,
        image_name
    )
    return url
