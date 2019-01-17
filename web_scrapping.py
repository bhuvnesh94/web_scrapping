#!/usr/bin/python3
import bs4

import requests
url="https://en.wikipedia.org/wiki/Helicopter"
#downloading web page using get request to web server
page_data=requests.get(url).content
#print(page_data)
