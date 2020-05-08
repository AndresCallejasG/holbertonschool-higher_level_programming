#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new = {}
    new = {key: (a_dictionary[key] * 2) for key in a_dictionary}
    return new
