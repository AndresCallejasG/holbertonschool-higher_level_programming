#!/usr/bin/python3
"""
    fetches https://intranet.hbtn.io/status
"""
import urllib.request


with urllib.request.urlopen('https://intranet.hbtn.io/status') as url_response:
    body = url_response.read()
    print("Body response:")
    print("\t- type: {}\n\t- content: {}".format(type(body), body))
    print("\t- utf8 content:", body.decode('utf-8'))
