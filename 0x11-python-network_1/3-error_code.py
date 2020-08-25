#!/usr/bin/python3
"""
    takes in a URL, sends a request to the URL
    and displays the body of the response
    manage urllib.error.HTTPError exceptions
"""
from urllib import request, error
import sys

if __name__ == '__main__':
    url = sys.argv[1]
    try:
        with request.urlopen(url) as url_response:
            body = url_response.read().decode('utf-8')
            print(body)
    except error.HTTPError as ex:
        print("Error code: {}".format(ex.code))
