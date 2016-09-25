import sys

from . import facets
from . import utils
from .products import get_product

openfoodfacts = sys.modules[__name__]
__version__ = '0.0.1'


def add_fetch_function(facet):
    """
    Generate a fetch_ function for given facet, a function that will download
    data for a given facet.

    Usage example for traces:

        openfoodfacts.facets.fetch_traces()
    """
    def func():
        return utils.fetch(facet)['tags']
    func.__name__ = "get_%s" % facet
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
    def func(facet_id):
        return utils.fetch('%s/%s' % (facet, facet_id))['products']
    func.__name__ = "get_by_%s" % facet
    setattr(products, func.__name__, func)

# Build a fetch function for each facet.
for facet in facets.facets:
    add_fetch_function(facet)
    add_by_facet_fetch_function(facet)
