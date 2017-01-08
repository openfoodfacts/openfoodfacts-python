# -*- coding: utf-8 -*-


def get_autosuggest_url(tag_type, language, geography):
    base_url = "http://" + geography + ".openfoodfacts.org"
    autosuggest = base_url + "/cgi/suggest.pl?lc=" + language + "&tagtype=" + tag_type
    return autosuggest
