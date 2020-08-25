#!/usr/bin/python3
"""
    fetches https://intranet.hbtn.io/status
"""
import requests

if __name__ == '__main__':

    body = requests.get('https://intranet.hbtn.io/status').text
    print("Body response:")
    print("\t- type: {}\n\t- content: {}".format(type(body), body))
