import requests
import re
import getpass
import sys
import urllib

API_URL = "https://%s.openfoodfacts.org/"
OBF_API_URL = "https://%s.openbeautyfacts.org/"
OPFF_API_URL = "https://%s.openpetfoodfacts.org/"


def login_into_OFF():
    # Get username and pasword
    username = raw_input('Username:')
    pswd = getpass.getpass('Password:')

    payload = {'user_id': username, 'password': pswd}

    # create a requests session
    with requests.Session() as c:

        # post the username and password on the website
        r = c.post(API_URL % ('world'), data=payload)

        # get the complete html text
        complete_html = r.text

        # check if login is successfull
        if re.search('You are connected as', complete_html) is None:
            raise ValueError('Incorrect Username or Password.')

        # Return the session object
        return c


def download_data(file_type='mongodb'):
    """
    Fetch data from Openfoodfacts server. Options mongodb, csv, rdf.
    The file is downloded in the current directory.
    """
    if file_type == 'mongodb':
        file_url = build_url(service='data',
                             resource_type='openfoodfacts-mongodbdump.tar.gz')
        filename = "openfoodfacts-mongodbdump.tar.gz"

    elif file_type == 'csv':
        file_url = build_url(service='data',
                             resource_type='en.openfoodfacts.org.products.csv')
        filename = "en.openfoodfacts.org.products.csv"

    elif file_type == 'rdf':
        file_url = build_url(service='data',
                             resource_type='en.openfoodfacts.org.products.rdf')
        filename = "en.openfoodfacts.org.products.rdf"

    request_content = requests.get(file_url, stream=True)

    with open(filename, "wb") as file:
        for chunk in request_content.iter_content(chunk_size=1024):

            # writing one chunk at a time to the file
            if chunk:
                file.write(chunk)


def build_url(geography='world', service=None,
              resource_type=None, parameters=None, entity="food"):

    if entity == "food":
        geo_url = API_URL % (geography)

    elif entity == "beauty":
        geo_url = OBF_API_URL % (geography)

    elif entity == "pet":
        geo_url = OPFF_API_URL % (geography)

    else:
        raise ValueError("Product not recognized!")

    geo_url = geo_url[:-1]

    if service == 'api':
        version = 'v0'
        base_url = "/".join([geo_url,
                             service,
                             version,
                             resource_type,
                             parameters])

    elif service == 'data':
        base_url = "/".join([geo_url, service, resource_type])

    elif service == 'cgi':
        if parameters is None:
            base_url = "/".join([geo_url, service, resource_type])

        else:
            sub_url = "/".join([geo_url, service, resource_type])
            if sys.version_info >= (3, 0):
                extension = urllib.parse.urlencode(parameters)
            else:
                extension = urllib.urlencode(parameters)

            base_url = "?".join([sub_url, extension])

    elif service is None:
        if type(resource_type) == list:
            resource_type = '/'.join(resource_type)
        base_url = "/".join(filter(None, (geo_url, resource_type, parameters)))

    else:
        raise ValueError("Service not found!")

    return base_url


def fetch(path, json_file=True):
    """
    Fetch data at a given path assuming that target match a json file and is
    located on the OFF API.
    """
    if json_file:
        path = "%s.json" % (path)

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
