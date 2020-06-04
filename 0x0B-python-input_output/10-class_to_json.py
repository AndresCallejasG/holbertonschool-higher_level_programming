#!/usr/bin/python3
""" Input/Output project
"""


def class_to_json(obj):
    """returns the dictionary description with simple data structure
        (list, dictionary, string, integer and boolean) for JSON
        serialization of an object

    Arguments:
        obj {object} -- object to be convert

    Returns:
        dictionary description
    """
    return obj.__dict__
