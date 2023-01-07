from difflib import get_close_matches
import json
from urllib.parse import urlencode

import requests
from bs4 import BeautifulSoup

with open('./city_links.json') as json_file:
    data = json.load(json_file)
city_list = list(data.keys())

# check if city there in citylinks
def is_station(city):
    return(city in city_list)

# get closest match
def closest_station(city):
    return(get_close_matches(city, city_list, n=10))

# get daily-data
def get_daily(city):
    pass
# get forecast


# one func to:

# return min-max temp

# return rainfall

# return humidity

# return suntime

# return moontime

# based on true false thingies