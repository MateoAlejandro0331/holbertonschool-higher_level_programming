#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    aux = matrix.copy()
    new = list(map(lambda x: list(map(lambda y: (y**2), x)), aux))
    return new
