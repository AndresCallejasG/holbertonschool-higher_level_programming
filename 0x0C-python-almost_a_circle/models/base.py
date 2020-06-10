#!/usr/bin/python3
""" Almost a circle project

"""


import json
import csv


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
        if list_objs and len(list_objs) > 0:
            for obj in list_objs:
                dic.append(obj.to_dictionary())
        with open(cls.__name__ + ".json", "w") as f:
            f.write(cls.to_json_string(dic))

    @staticmethod
    def from_json_string(json_string):
        """ that returns the list of the JSON string
            representation json_string

        Args:
            json_string (str): string representing a list of dictionaries

        Returns:
            If json_string is None or empty, return an empty list
            Otherwise, return the list represented by json_string
        """
        if json_string and len(json_string) > 0:
            return json.loads(json_string)
        return []

    @classmethod
    def create(cls, **dictionary):
        """ uses the update method to assign all attributes
            returns an instance with all attributes already set

        Returns:
            new_object (cls): instance with all attributes already set
        """
        if cls.__name__ == "Rectangle":
            new_obj = cls(1, 1)
        else:
            new_obj = cls(1)
        new_obj.update(**dictionary)
        return new_obj

    @classmethod
    def load_from_file(cls):
        """ returns a list of instances from a file

        Returns:
                If the file doesn’t exist, return an empty list
                Otherwise, return a list of instances.
                The type of these instances depends on cls

        """
        try:
            with open(cls.__name__ + ".json", "r") as f:
                data = f.read()
                data = cls.from_json_string(data)
            return [cls.create(**elem) for elem in data]
        except:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """ serializes list_objs in CSV file
        """
        dict_list = [obj.to_dictionary() for obj in list_objs]
        with open(cls.__name__ + ".csv", "w") as file:
            write = csv.DictWriter(file, dict_list[0].keys())
            write.writeheader()
            write.writerows(dict_list)

    @classmethod
    def load_from_file_csv(cls):
        """ deserializes from CSV file
        """
        try:
            list_objs = []
            dictionary = {}
            with open(cls.__name__ + ".csv", "r") as file:
                csv_text = csv.DictReader(file)
                for elem in csv_text:
                    for k, v in dict(elem).items():
                        dictionary[k] = int(v)
                    list_objs.append(cls.create(**dictionary))
        except:
            pass
        finally:
            return list_objs
