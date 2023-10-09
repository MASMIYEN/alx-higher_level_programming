#!/usr/bin/python3
"""defines function that devides matrix elements"""


def matrix_divided(matrix, div):
    """Divides all elements of matrix"""
    errmsg = "matrix must be a matrix (list of lists) of integers/floats"
    if (not isinstance(matrix, list)) or (not matrix):
        raise TypeError(errmsg)
    for i in matrix:
        if not isinstance(i, list) or (not i):
            raise TypeError(errmsg)
        for j in i:
            if not isinstance(j, int) and not isinstance(j, float):
                raise TypeError(errmsg)
        if not all(len(row) == len(matrix[0]) for row in matrix):
            raise TypeError("Each row of the matrix must have the same size")
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    div_matrix = [[round(j / div, 2) for j in i] for i in matrix]

    return div_matrix
