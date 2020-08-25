#!/usr/bin/python3
"""
    takes in a URL and an email, sends a POST request
    to the passed URL with the email as a parameter,
    and displays the body of the response
"""
from urllib import request, parse
import sys

if __name__ == '__main__':
    url = sys.argv[1]
    email = parse.urlencode({"email": sys.argv[2]}).encode('utf-8')
    with request.urlopen(url, email) as url_response:
        body = url_response.read().decode('utf-8')
        print(body)
