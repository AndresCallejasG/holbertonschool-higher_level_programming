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

    def __str__(self):
        """ returns [Square] (<id>) <x>/<y> - <size>
        """
        string = "[Square]"
        string += " ({:d}) {:d}/{:d} ".format(self.id, self.x, self.y)
        string += "- {:d}".format(self.height)
        return string
