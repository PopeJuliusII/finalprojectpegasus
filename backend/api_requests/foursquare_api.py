import requests
from bs4 import BeautifulSoup
import lxml

# curl -i -X GET "https://api.foursquare.com/v2/venues/search?&client_id=SPJKIIRUO1MO0VEZQ4YC1VBIGUVJ3IBVYQIS5MWLRO0D53K0&client_secret=JAISUVIQTX44KNXZ0N2FOMJ1FCKARINB5OCFLJWQ1XVAU42V&ll=40.751750,-73.979593&v=20200404"

a = requests.get(f"https://api.foursquare.com/v2/venues/search?&client_id=SPJKIIRUO1MO0VEZQ4YC1VBIGUVJ3IBVYQIS5MWLRO0D53K0&client_secret=JAISUVIQTX44KNXZ0N2FOMJ1FCKARINB5OCFLJWQ1XVAU42V&ll=40.751750,-73.979593&v=20200404&limit=50&radius=100").text
soup = BeautifulSoup(a, 'lxml')
print(soup)
"""
{"id": "5aaaad2f1543c7069f56190f",
 "name": "Dill & Parsley",
 "location": {"address": "295 Madison Avenue",
             "crossStreet": "41st",
             "lat": 40.751760482595444,
             "lng": -73.97933212848565, "
             labeledLatLngs":[{"label":"display",
                               "lat": 40.751760482595444,
                               "lng": -73.97933212848565}],
                               "distance": 22,
                               "postalCode": "10017",
                               "cc": "US",
                               "city": "New York",
                               "state": "NY",
                               "country": "United States",
                               "formattedAddress": ["295 Madison Avenue (41st)",
                                                   "New York, NY 10017",
                                                   "United States"]},
 "categories": [{"id": "4bf58dd8d48988d1c0941735", "name": "Mediterranean Restaurant", "pluralName": "Mediterranean Restaurants", "shortName": "Mediterranean", "icon": {"prefix": "https:\/\
/ss3.4sqi.net\/img\/categories_v2\/food\/mediterranean_", "suffix": ".png"}, "primary": true}], "referralId": "v-1586793961", "hasPerk": false}
"""
