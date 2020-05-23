#!/urs/python3
"""
This is the "add integer" module.
This is one of the task from TDD project - Holberton School

"""


def add_integer(a, b=98):
    """ function that adds 2 integers.
        first casting them to integers if they are float
    """
    if type(a) not in [float, int]:
        raise TypeError("a must be an integer")
    elif isinstance(a, float):
        a = int(a)
    if type(b) not in [float, int]:
        raise TypeError("a must be an integer")
    elif isinstance(b, float):
        b = int(b)
    return a + b
