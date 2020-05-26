#!/usr/bin/python3
"""
More classes and Objects - Holberton School
Defines a Rectangle
"""


class Rectangle:
    """
    Rectangle class

    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """init function with validation using setters

        Arguments:
            width --> int
            height --> int

        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    def __del__(self):
        """
        del function
        says bye!
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

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

    def area(self):
        """returns the current rectangle area"""
        my_area = self.__width * self.__height
        return my_area

    def perimeter(self):
        """returns the current rectangle perimeter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        my_perimeter = 2 * self.__width + 2 * self.__height
        return my_perimeter

    def __str__(self):
        """
        returns the rectangle with the character #
        """
        rect_str = ""
        if self.__width != 0 and self.__height != 0:
            symbol = str(self.print_symbol)
            rect_str = ((symbol * self.width + "\n") * (self.height - 1))
            rect_str += symbol * self.width
        return rect_str

    def __repr__(self):
        """
        returns the respresentation of a rectangle
        you can create a new instance based on representation:
            new_rectangle = eval(repr(my_rectangle))
        """
        return ("Rectangle({:d}, {:d})".format(self.__width, self.__height))
