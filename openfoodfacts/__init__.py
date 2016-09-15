import facets
import utils
import sys
from products import get_product

openfoodfacts = sys.modules[__name__]
__version__ = '0.0.1'


"""
Generate a fetch_ function for given facet, a function that will download data
for a given facet.

usage example for traces:

    openfoodfacts.fetch_traces()
"""
def add_fetch_function(facet):
    def func():
        return utils.fetch(facet)['tags']
    func.__name__ = "get_%s" % facet
    setattr(openfoodfacts, func.__name__, func)


# Build a fetch function for each facet.
for facet in facets.facets:
    add_fetch_function(facet)
