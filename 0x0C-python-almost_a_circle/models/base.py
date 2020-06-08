#!/usr/bin/python3
""" Almost a circle project

"""


import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """ returns the JSON string representation of list_dictionaries

        Args:
            list_dictionaries (dict)

        Returns:
            If list_dictionaries is None or empty, return the string: "[]"
            Otherwise, return the JSON string representation of
            list_dictionaries

        """
        if list_dictionaries and len(list_dictionaries) > 0:
            return json.dumps(list_dictionaries)
        return "[]"

    @classmethod
    def save_to_file(cls, list_objs):
        """ writes the JSON string representation of list_objs
            to a file, If list_objs is None, save an empty list

        Args:
            list_objs: a list of instances who inherits of Base
        """
        dic = []
        if list_objs:
            for obj in list_objs:
                dic.append(obj.to_dictionary())
        with open(cls.__name__ + ".json", "w") as f:
            f.write(cls.to_json_string(dic))
