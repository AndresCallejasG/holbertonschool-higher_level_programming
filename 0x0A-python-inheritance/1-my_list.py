#!/usr/bin/python3
"""Inheritance project

"""


class MyList(list):
    """class that inherits from list
    """
    def print_sorted(self):
        """prints itself (sorted)

        """
        print(sorted(self))
