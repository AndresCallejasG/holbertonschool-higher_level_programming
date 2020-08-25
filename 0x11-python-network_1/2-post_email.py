#!/usr/bin/python3
"""
    takes in a URL, sends a request to the URL
    and displays the value of the X-Request-Id
"""
from urllib import request, parse
import sys

if __name__ == '__main__':
    url = sys.argv[1]
    email = parse.urlencode({"email": sys.argv[2]}).encode('utf-8')
    with request.urlopen(url, email) as url_response:
        body = url_response.read().decode('utf-8')
        print(body)
