#!/usr/bin/python3
""" Input/Output project
"""


def read_file(filename=""):
    """ reads a given file - UTF8

    Keyword Arguments:
        filename {file} -- file to be read (default: {""})
    """
    with open(filename,  encoding='utf-8') as f:
        print(f.read(), end="")
