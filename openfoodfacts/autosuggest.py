# -*- coding: utf-8 -*-


def get_autosuggest_url(tag_type, language, geography):
    autosuggest = "http://" + geography + ".openfoodfacts.org/cgi/suggest.pl?lc=" + language + "&tagtype=" + tag_type
    return autosuggest
