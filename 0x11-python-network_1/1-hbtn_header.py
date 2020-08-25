#!/usr/bin/python3
"""
    takes in a URL, sends a request to the URL
    and displays the value of the X-Request-Id
"""
import urllib.request
import sys

url = sys.argv[1]
with urllib.request.urlopen(url) as url_response:
    header = url_response.getheader('X-Request-Id')
    print(header)
