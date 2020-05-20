#!/usr/bin/python3
""" my first class """


class Square:
    """square with size"""

    def __init__(self, size=0, position=(0, 0)):
        """init function with validation --> positive int"""
        self.__size = size
        self.__position = position

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

    def my_print(self):
        """function to print the square using # """
        if self.__size > 0:
            for i in range(self.__position[1]):
                print()
            for i in range(self.__size):
                print(" " * self.__position[0], end="")
                print("#" * self.__size)
        else:
            print()

    @property
    def position(self):
        """position getter"""
        return self.__position

    @position.setter
    def position(self, value):
        """position setter """
        if (isinstance(value, tuple) and len(value) == 2 and
                isinstance(value[0], int) and value[0] >= 0 and
                isinstance(value[1], int) and value[1] >= 0):
                self.__position = value
        else:
            raise TypeError("position must be a tuple of 2 positive integers")
