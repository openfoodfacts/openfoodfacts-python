# -*- coding: utf-8 -*-


def get_autosuggest_url(tag_type, language, geography):
    base_url = "https://" + geography + ".openfoodfacts.org"
    autosuggest = base_url + "/cgi/suggest.pl?lc=" + language
    autosuggest += "&tagtype=" + tag_type
    return autosuggest
