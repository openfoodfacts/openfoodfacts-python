class FacetContainer:
    """
    Container class for Facets to handle pagination and data manipulation.
    Related to Issue #106 and #56.
    """
    def __init__(self, data=None):
        self.data = data or []
        self.page = 1