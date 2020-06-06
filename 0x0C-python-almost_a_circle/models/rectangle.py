#!/usr/bin/python3
""" Almost a circle project

"""


from models.base import Base


class Rectangle(Base):
    """ class Rectangle that inherits from Base
        Call the super class with id
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ init method

        Args:
            width (int)
            height (int)
            x (int, optional):  Defaults to 0.
            y (int, optional):  Defaults to 0.
            id (int, optional):  Defaults to None.
        """
        if id is not None:
            Base.__init__(self, id)
        else:
            Base.__init__(self)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

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
                raise ValueError("width must be > 0")
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
                raise ValueError("height must be > 0")
        else:
            raise TypeError("height must be an integer")

    @property
    def x(self):
        """x getter"""
        return self.__x

    @x.setter
    def x(self, value):
        """x.setter"""
        if isinstance(value, int):
            if value >= 0:
                self.__x = value
            else:
                raise ValueError("x must be >= 0")
        else:
            raise TypeError("x must be an integer")

    @property
    def y(self):
        """y getter"""
        return self.__y

    @y.setter
    def y(self, value):
        """y.setter"""
        if isinstance(value, int):
            if value >= 0:
                self.__y = value
            else:
                raise ValueError("y must be >= 0")
        else:
            raise TypeError("y must be an integer")

    def area(self):
        """ function area
        """
        return self.__width * self.__height