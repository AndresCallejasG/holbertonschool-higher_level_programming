#!/usr/bin/python3
""" Input/Output project
"""


def read_lines(filename="", nb_lines=0):
    """ reads n lines from a given file and prints them- UTF8
        if n == 0 prints the whole file

    Keyword Arguments:
        filename {str} -- file to be read (default: {""})
        nb_lines {int} -- number of lines (default: {0})
    """

    with open(filename,  encoding='utf-8') as f:
        lines = f.readlines()
        if nb_lines <= 0:
            nb_lines = len(lines)
        print("".join(lines[0:nb_lines]), end="")
