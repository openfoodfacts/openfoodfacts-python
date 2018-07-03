import sys

from . import facets
from . import utils
from .products import get_product
from . import openbeautyfacts
from . import openpetfoodfacts

openfoodfacts = sys.modules[__name__]
__version__ = '0.1.0'


def add_fetch_function(facet):
    """
    Generate a fetch_ function for given facet, a function that will download
    data for a given facet.

    Usage example for traces:

        openfoodfacts.facets.fetch_traces()
    """
    def func(locale='world'):
        path = utils.build_url(geography=locale,
                               resource_type=facet)

        if facet == "ingredients":
            return utils.fetch(path)['products']

        return utils.fetch(path)['tags']

    func.__name__ = "get_%s" % facet

    if func.__name__ == "get_purchase_places":
        facet = "purchase-places"
    elif func.__name__ == "get_packaging_codes":
        facet = "packager-codes"
    elif func.__name__ == "get_entry_dates":
        facet = "entry-dates"

    setattr(facets, func.__name__, func)


def add_by_facet_fetch_function(facet):
    """
    Generate a fetch_by_ function for given facet, a function that will
    download data for a given facet.

    Usage example for egg trace:

        openfoodfacts.products.get_by_trace(egg)
    """
    if facet[-3:] == 'ies':
        facet = facet[:-3] + 'y'
    else:
        facet = facet[:-1]

    def func(facet_id, page=1, locale='world'):

        path = utils.build_url(geography=locale,
                               resource_type=[facet, facet_id, str(page)])

        return utils.fetch(path)['products']

    func.__name__ = "get_by_%s" % facet
    setattr(products, func.__name__, func)


# Build a fetch function for each facet.
for facet in facets.facets:
    add_fetch_function(facet)
    add_by_facet_fetch_function(facet)
