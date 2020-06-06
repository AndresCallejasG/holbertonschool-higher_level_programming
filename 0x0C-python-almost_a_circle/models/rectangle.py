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

    def display(self):
        """
            returns the rectangle with the character #
        """
        symbol = "#"
        rect_str = ""
        rect_str = ((symbol * self.__width + "\n") * (self.__height - 1))
        rect_str += symbol * self.__width
        print(rect_str)

    def __str__(self):
        """ returns [Rectangle] (<id>) <x>/<y> - <width>/<height>
        """
        string = "[Rectangle]"
        string += " ({:d}) {:d}/{:d} ".format(self.id, self.__x, self.__y)
        string += "- {:d}/{:d}".format(self.__width, self.__height)
        return string

    def update(self, *args, **kwargs):
        """ assigns an argument to each attribute

            1st argument should be the id attribute
            2nd argument should be the width attribute
            3rd argument should be the height attribute
            4th argument should be the x attribute
            5th argument should be the y attribute
        """
        if (args):
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.width = args[1]
            if len(args) >= 3:
                self.height = args[2]
            if len(args) >= 4:
                self.x = args[3]
            if len(args) >= 5:
                self.y = args[4]
        elif(kwargs):
            for k, v in kwargs.items():
                if k == "id":
                    self.id = v
                if k == "width":
                    self.__width = v
                if k == "height":
                    self.__height = v
                if k == "x":
                    self.__x = v
                if k == "y":
                    self.__y = v
