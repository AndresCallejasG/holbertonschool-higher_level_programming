#!/usr/bin/python3
""" Input/Output project
"""


import json


def save_to_json_file(my_obj, filename):
    """ writes an Object to a text file, using a JSON representation:

    Arguments:
        my_obj {object} -- object to be written
        filename {string} -- file to be written to
    """
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(my_obj, f)
