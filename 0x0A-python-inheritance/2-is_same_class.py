#!/usr/bin/python3
"""Inheritance project

"""


def is_same_class(obj, a_class):
    """checks if the object is instance of the given class

    Arguments:
        obj -- given object
        a_class -- given class
    """
    return type(obj) is a_class
