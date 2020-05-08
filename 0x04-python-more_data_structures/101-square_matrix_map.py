#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    new = list(map(lambda row: list(map(lambda n: n * n, row)), matrix))
    return new
