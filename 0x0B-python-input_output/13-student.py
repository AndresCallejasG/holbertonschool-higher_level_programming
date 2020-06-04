#!/usr/bin/python3
""" Input/Output project
"""


class Student:
    """Student class - defined by first name, last name and age
    """

    def __init__(self, first_name, last_name, age):
        """ init_method

        Arguments:
            first_name {str} -- student's first name
            last_name {str} -- student's last name
            age {int} -- student's age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ retrieves a dictionary representation of a Student instance
        """
        if attrs is None or type(attrs) is not list:
            return self.__dict__
        for i in attrs:
            if not isinstance(i, str):
                return self.__dict__

        return {key: val for key, val in self.__dict__.items() if key in attrs}

    def reload_from_json(self, json):
        """replace all attributes of instance student
        """
        self.__dict__.update(json)
