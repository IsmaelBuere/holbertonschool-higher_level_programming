#!/usr/bin/python3
"""
Write a function that adds 2 integers
"""


def add_integer(a, b=98):
    """
    Adds two numbers who should are integers.
    """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    a = int(a)
    b = int(b)

    return a + b
