#!/usr/bin/python3
""" Input/Output project
"""


def write_file(filename="", text=""):
    """ writes a string to a text file (UTF8)
        returns the number of characters written

    Keyword Arguments:
        filename {str} -- file to be written to (default: {""})
        text {str} -- str to be written (default: {""})
    """

    with open(filename, 'w', encoding='utf-8') as f:
        return f.write(text)
