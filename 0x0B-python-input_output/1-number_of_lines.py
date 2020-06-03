#!/usr/bin/python3
""" Input/Output project
"""


def number_of_lines(filename=""):
    """ reads a given file and return the number of lines - UTF8

    Keyword Arguments:
        filename {file} -- file to be read (default: {""})
    """
    with open(filename,  encoding='utf-8') as f:
        return len(f.readlines())
