#!/usr/bin/python3
""" Input/Output project
"""


import json


def to_json_string(my_obj):
    """ returns the JSON representation of an object (string)

    Arguments:
        my_obj {obj} -- object to be printed
    """
    return json.dumps(my_obj)
