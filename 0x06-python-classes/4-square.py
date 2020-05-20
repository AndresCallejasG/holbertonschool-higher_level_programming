#!/usr/bin/python3
""" my first class """


class Square:
    """square with size"""

    def __init__(self, size=0):
        """init function with validation --> positive int"""
        self.__size = size

    def area(self):
        """returns the current square area"""
        my_area = self.__size ** 2
        return my_area

    @property
    def size(self):
        """size getter"""
        return self.__size

    @size.setter
    def size(self, value):
        """size.setter"""
        if isinstance(value, int):
            if value >= 0:
                self.__size = value
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")
