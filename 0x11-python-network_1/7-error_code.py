#!/usr/bin/python3
"""
    takes in a URL and an email address, sends a POST request
    to the passed URL with the email as a parameter and
    displays the body of the response.
"""
import requests
import sys

if __name__ == '__main__':
    url = sys.argv[1]
    body = requests.get(url)
    status = body.status_code
    if status >= 400:
        print("Error code: {}".format(status))
    else:
        print(body.text)
