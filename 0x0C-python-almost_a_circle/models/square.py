#!/usr/bin/python3
""" Almost a circle project

"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """ class Square that inherits from Rectangle
        Call the super class with id, x, y, width and height
        The width and height must be assigned to the value of size
    """

    def __init__(self, size, x=0, y=0, id=None):
        """ init method

        Args:
            size (int)
            x (int, optional):  Defaults to 0.
            y (int, optional):  Defaults to 0.
            id (int, optional):  Defaults to None.
        """
        Rectangle.__init__(self, size, size, x, y, id)

    @property
    def size(self):
        """size getter - uses width
        """
        return self.width

    @size.setter
    def size(self, value):
        """ size.setter
            same value validation as the Rectangle for width and height
        """
        self.width = value
        self.height = value

    def __str__(self):
        """ returns [Square] (<id>) <x>/<y> - <size>
        """
        string = "[Square]"
        string += " ({:d}) {:d}/{:d} ".format(self.id, self.x, self.y)
        string += "- {:d}".format(self.height)
        return string

    def update(self, *args, **kwargs):
        """ assigns an argument to each attribute

            1st argument should be the id attribute
            2nd argument should be the size attribute
            3rd argument should be the x attribute
            4th argument should be the y attribute
        """
        if (args):
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.size = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) >= 4:
                self.y = args[3]
        elif(kwargs):
            for k, v in kwargs.items():
                if k == "id":
                    self.id = v
                if k == "size":
                    self.size = v
                if k == "x":
                    self.x = v
                if k == "y":
                    self.y = v

    def to_dictionary(self):
        """ returns the Square's dictionary representation
            alternatives:
                vars(self)
                self.__dict__

        Returns:
            dict: dictionary representation of a Square
        """
        my_dict = {}
        for attr in ["id", "size", "x", "y"]:
            my_dict.update({attr: getattr(self, attr)})
        return my_dict
