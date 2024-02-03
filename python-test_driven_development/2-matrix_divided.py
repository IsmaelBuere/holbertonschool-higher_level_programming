#!/usr/bin/python3
"""
Defines a matrix division function.
"""


def matrix_divided(m, div):
    """
    Divides all elements of a matrix.
    """
    err = "matrix must be a matrix (list of lists) of integers/floats"
    if not isinstance(m, list) or not all(isinstance(r, list) for r in m):
        raise TypeError(err)
    if not all(isinstance(i, (int, float)) for r in m for i in r):
        raise TypeError(err)
    if not all(len(r) == len(m[0]) for r in m):
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(i / div, 2) for i in r] for r in m]
