#!/usr/bin/python3
""" my first class """


class Square:
    """square with size"""

    def __init__(self, size=0):
        """init function with validation --> positive int"""
        if isinstance(size, int):
            if size >= 0:
                self.__size = size
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")

    def area(self):
        """returns the current square area"""
        my_area = self.__size ** 2
        return my_area
