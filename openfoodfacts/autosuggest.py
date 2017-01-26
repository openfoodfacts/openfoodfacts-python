# -*- coding: utf-8 -*-


def get_autosuggest_url(tag_type, language, geography):
    base_url = "https://" + geography + ".openfoodfacts.org"
    autosuggest = base_url + "/cgi/suggest.pl"
    params = "?lc=" + language + "&tagtype=" + tag_type
    url = autosuggest + params
    return url
