#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new = []
    new = [[n*n for n in row] for row in matrix]
    return new
