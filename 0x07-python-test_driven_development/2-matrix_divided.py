#!/usr/bin/python3
""" 

Funtion to divide a matrix and return a new matrix

"""


def matrix_divided(matrix, div):
    """ 
    All validations to the functions
    """
    new_matrix = []
    Error_list = "matrix must be a matrix (list of lists) of integers/floats"
    if not matrix:
        raise TypeError(Error_list)
    if type(matrix) is not list:
        raise TypeError(Error_list)
    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    if  div == 0:
        raise ZeroDivisionError("division by zero")
    for row in matrix:
        if type(row) is not list:
            raise TypeError(Error_list)
        if row is None:
            raise TypeError(Error_list)
        for element in row:
            if type(element) is not int and type(element) is not float:
                raise TypeError(Error_list)
        if not all(len(row) is len(matrix[0]) for row in matrix):
            raise TypeError("Each row of the matrix must have the same size")
        new_matrix.append(list(map(lambda element: round(element / div, 2), row)))
    return new_matrix
