import requests
import re


def scrape_foursquare_categories():
    return re.findall(r'icon"/><h3>([\w\s]*)</h3><p>(\w*)</p>', requests.get(
        'https://developer.foursquare.com/docs/build-with-foursquare/categories/').text)
