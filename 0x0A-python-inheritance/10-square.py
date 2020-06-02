#!/usr/bin/python3
"""Inheritance project

"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ Square class, inherts from Rectangle
    """
    def __init__(self, size):
        """ init method

        Arguments:
            size {int} -- Square's size
        """
        super().integer_validator("size", size)
        self.__size = size
        super().__init__(self.__size, self.__size)

    def area(self):
        """function area
        """
        result = self.__size ** 2
        return result
