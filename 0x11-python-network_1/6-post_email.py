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
    parameters = {'email': sys.argv[2]}
    body = requests.post(url, data=parameters)
    print(body.text)
