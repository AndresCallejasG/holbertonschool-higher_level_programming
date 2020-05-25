#!/usr/bin/python3
"""
More classes and Objects - Holberton School
Defines a Rectangle
"""


class Rectangle:
    """
    Rectangle class

    """

    def __init__(self, width=0, height=0):
        """init function with validation using setters

        Arguments:
            width --> int
            height --> int

        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """width getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """width.setter"""
        if isinstance(value, int):
            if value >= 0:
                self.__width = value
            else:
                raise ValueError("width must be >= 0")
        else:
            raise TypeError("width must be an integer")

    @property
    def height(self):
        """height getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """height.setter"""
        if isinstance(value, int):
            if value >= 0:
                self.__height = value
            else:
                raise ValueError("height must be >= 0")
        else:
            raise TypeError("height must be an integer")
