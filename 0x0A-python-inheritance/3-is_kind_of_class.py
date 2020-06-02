#!/usr/bin/python3
"""Inheritance project

"""


def is_kind_of_class(obj, a_class):
    """ returns True if the object is an instance of, or if the object
        is an instance of a class that inherited from

    Arguments:
        obj -- given object
        a_class -- given class
    """
    return isinstance(obj, a_class)
