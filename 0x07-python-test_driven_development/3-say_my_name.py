#!/urs/python3
"""
This is the "say_my_name" module.
One of the tasks from TDD project - Holberton School

"""


def say_my_name(first_name, last_name=""):
    """
        function that prints My name is <first name> <last name>

    """
    if type(first_name) is not str or first_name is None:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
