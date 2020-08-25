#!/usr/bin/python3
"""
    takes in a letter and sends a POST request to
    http://0.0.0.0:5000/search_user with the letter
    as a parameter.
"""
import requests
import sys

if __name__ == '__main__':

    url = 'http://0.0.0.0:5000/search_user'
    args = {'q': ""}
    if len(sys.argv) > 1:
        args['q'] = sys.argv[1]

    body = requests.post(url, args)

    try:
        b_json = body.json()
        if b_json:
            print("[{}] {}".format(b_json['id'], b_json['name']))
        else:
            print("No result")

    except:
        print("Not a valid JSON")
