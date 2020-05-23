#!/urs/python3
"""
This is the "matrix_divided" module.
One of the tasks from TDD project - Holberton School

"""


def matrix_divided(matrix, div):
    """
        function that divides all elements of a matrix by a given number

    """

    terror_msg = "matrix must be a matrix (list of lists) of integers/floats"

    if not isinstance(matrix, list):
        raise TypeError(terror_msg)
    if not isinstance(div, int):
        raise TypeError("div must be a number")
    elif div == 0:
        raise ZeroDivisionError("division by zero")
    for row in matrix:
        if not isinstance(row, list):
            raise TypeError(terror_msg)
        if len(matrix[0]) != len(row):
            raise TypeError("Each row of the matrix must have the same size")
        for elem in row:
            if not isinstance(elem, (int, float)):
                raise TypeError(terror_msg)
    row = []
    new = [[round((n / div), 2) for n in row] for row in matrix]
    return new
