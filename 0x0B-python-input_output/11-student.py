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

    def to_json(self):
        """ retrieves a dictionary representation of a Student instance
        """
        return self.__dict__
