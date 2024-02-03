#!/usr/bin/python3
"""
define a square
"""


def print_square(size):
    """
    Prints a square pattern made of '#' characters with the specified size.
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for _ in range(size):
        print("#" * size)
