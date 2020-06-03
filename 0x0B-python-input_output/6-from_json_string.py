#!/usr/bin/python3
""" Input/Output project
"""


import json


def from_json_string(my_str):
    """ returns an object (Python data structure) represented
        by a JSON string:

    Arguments:
        my_str {str} -- JSON string
    """
    return json.loads(my_str)
