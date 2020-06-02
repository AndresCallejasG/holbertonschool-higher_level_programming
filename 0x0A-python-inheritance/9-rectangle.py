#!/usr/bin/python3
"""Inheritance project

"""


BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """ Rectangle class, inherts from BaseGeometry
    """
    def __init__(self, width, height):
        """init method

        Arguments:
            width {[type]} -- Rectangle width
            height {[type]} -- Rectangle height
        """
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        """function area
        """
        result = self.__width * self.__height
        return result

    def __str__(self):
        """str function override
        """
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)
