import requests
import getpass
import sys
import urllib


API_URL = "https://%s.openfoodfacts.org/"
OBF_API_URL = "https://%s.openbeautyfacts.org/"
OPFF_API_URL = "https://%s.openpetfoodfacts.org/"

FILE_TYPE_MAP = {
    "mongodb": "openfoodfacts-mongodbdump.tar.gz",
    "csv": "en.openfoodfacts.org.products.csv",
    "rdf": "en.openfoodfacts.org.products.rdf"
}

ENTITY_MAP = {
    "food": API_URL,
    "beauty": OBF_API_URL,
    "pet": OPFF_API_URL
}


def login_into_OFF():
    username = raw_input("Username:")
    password = getpass.getpass("Password:")
    return login(username, password)


def login(username, password):
    """
    Login user with given credentials. Return related session.
    """
    payload = {"user_id": username, "password": password}

    with requests.Session() as session:
        request = session.post(API_URL % ("world"), data=payload)
        request_body = request.text
        if "You are connected as" not in request_body:
            raise ValueError("Incorrect Username or Password.")

        return session


def download_data(file_type="mongodb"):
    """
    Fetch data from Openfoodfacts server. Options mongodb, csv, rdf.
    The file is downloded in the current directory.
    """

    if file_type not in FILE_TYPE_MAP:
        raise ValueError("File type not recognized!")

    filename = FILE_TYPE_MAP[file_type]
    file_url = build_url(service="data", resource_type=filename)
    request_content = requests.get(file_url, stream=True)

    with open(filename, "wb") as target_file:
        for chunk in request_content.iter_content(chunk_size=1024):
            # writing one chunk at a time to the file
            if chunk:
                target_file.write(chunk)


def build_url(geography="world", service=None,
              resource_type=None, parameters=None, entity="food"):

    if entity not in ENTITY_MAP:
        raise ValueError("Product not recognized!")

    geo_url = ENTITY_MAP[entity] % geography
    geo_url = geo_url[:-1]

    if service == "api":
        version = "v0"
        base_url = "/".join([geo_url,
                             service,
                             version,
                             resource_type,
                             parameters])

    elif service == "data":
        base_url = "/".join([geo_url, service, resource_type])

    elif service == "cgi":
        base_url = "/".join([geo_url, service, resource_type])

        if parameters is not None:
            if sys.version_info >= (3, 0):
                extension = urllib.parse.urlencode(parameters)
            else:
                extension = urllib.urlencode(parameters)
            base_url = "?".join([base_url, extension])

    elif service is None:
        if type(resource_type) == list:
            resource_type = "/".join(resource_type)
        if resource_type == "ingredients":
            resource_type = "/".join(["state",  "complete", resource_type])
            parameters = "1"
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
