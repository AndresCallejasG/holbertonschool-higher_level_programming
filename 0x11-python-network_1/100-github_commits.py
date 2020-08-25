#!/usr/bin/python3
"""
    lists 10 commits (from the most recent to oldest) of
    the repository “rails” by the user “rails”
"""
import requests
import sys


if __name__ == "__main__":

    url = 'https://api.github.com/repos/'
    full_path = url + "{}/{}/commits".format(sys.argv[2], sys.argv[1])
    body = requests.get(full_path)
    for elem in body.json()[0:10]:
        sha = elem.get('sha')
        author = elem.get('commit').get('author').get('name')
        print("{}: {}".format(sha, author))
