#!/usr/bin/python3
"""
    takes your Github credentials (username and password) and
    uses the Github API to display your id
"""
import requests
import sys


if __name__ == "__main__":

    url = 'https://api.github.com/user'
    body = requests.get(url, auth=(sys.argv[1], sys.argv[2]))
    id = body.json().get("id")
    print(id)
