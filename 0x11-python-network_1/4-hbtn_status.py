#!/usr/bin/python3
"""
    fetches https://intranet.hbtn.io/status
"""
from urllib import request

if __name__ == '__main__':
    with request.urlopen('https://intranet.hbtn.io/status') as url_response:
        body = url_response.read()
        print("Body response:")
        print("\t- type: {}\n\t- content: {}".format(type(body), body))
        print("\t- utf8 content:", body.decode('utf-8'))
