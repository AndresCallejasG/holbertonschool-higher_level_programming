#!/usr/bin/python3
""" Almost a circle project

"""

    
class Base():
    """ Base class - The goal of it is to manage id attribute in all
        future classes and to avoid duplicating the same code
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """ init method

        Args:
            id ([type], optional): [description]. Defaults to None.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
