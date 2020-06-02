#!/usr/bin/python3
"""Inheritance project

"""


class BaseGeometry():
    """ Improved Geometry
    """
    def area(self):
        """returns area - not implemented yet
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates that value is a positive int

        Arguments:
            name {string} -- always a string
            value {int} -- given value to validate
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
