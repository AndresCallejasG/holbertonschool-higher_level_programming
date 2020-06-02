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
            width {[type]} -- Rentangle width
            height {[type]} -- Rentangle height
        """
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height
