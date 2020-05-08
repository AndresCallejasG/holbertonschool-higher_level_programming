#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    a_dict_copy = dict(a_dictionary)
    for elem in a_dict_copy:
        if a_dictionary[elem] == value:
            del a_dictionary[elem]
    return a_dictionary
