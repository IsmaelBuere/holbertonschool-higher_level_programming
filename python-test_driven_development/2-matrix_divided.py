#!/usr/bin/python3
"""
Write a function that divides all elements of a matrix.
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a given divisor.
    """

    error = "matrix must be a matrix (list of lists) of integers/floats"
    if not isinstance(matrix, list):
        raise TypeError(error)
    for i in matrix:
        if not isinstance(i, list):
            raise TypeError(error)
        for j in i:
            if not isinstance(j, (float, int)):
                raise TypeError(error)

    ref_row = len(matrix[0])
    for i in matrix:
        if len(i) != ref_row:
            raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (float, int)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(j / div, 2) for j in i] for i in matrix]
