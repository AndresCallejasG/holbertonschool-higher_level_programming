#!/usr/bin/python3
"""Inheritance project
"""


def add_attribute(obj, name, value):
    """adds a new attribute to an object if it’s possible

    Arguments:
        obj -- given object
        name -- attribute name
        value -- attribute value

    Raises:
        TypeError: if the object can’t have new attribute
    """

    if hasattr(obj, "__dict__"):
        setattr(obj, name, value)
    else:
        raise TypeError("can't add new attribute")
