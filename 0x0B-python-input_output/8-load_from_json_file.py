#!/usr/bin/python3
""" Input/Output project
"""


import json


def load_from_json_file(filename):
    """ creates an Object from a “JSON file”

    Arguments:
        filename {string} -- file to read from
    """
    with open(filename, encoding='utf-8') as f:
        return json.load(f)
