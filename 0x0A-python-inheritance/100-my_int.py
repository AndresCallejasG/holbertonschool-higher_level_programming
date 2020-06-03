#!/usr/bin/python3
"""Inheritance project
"""


class MyInt(int):
    """ Class that inherits int with == and != operators inverted

    Arguments:
        int {object}
    """

    def __init__(self, value):
        self.__value = value

    def __eq__(self, value):
        return self.__value != value

    def __ne__(self, value):
        return self.__value == value
