import utils


SEARCH_PATH = "cgi/search.pl"

"""
Return information of a given product.
"""
def get_product(barcode):
    return utils.fetch('api/v0/product/%s' % barcode)


"""
Perform a search using Open Food Facts search engine.
"""
def search(query, pagination=20):
    pass
