#!/usr/bin/python3
'''
Write a function that adds 2 integers
'''


def add_integer(a, b=98):
    '''
    Adds two integers
    '''
    TypeError - if a or b are not integers or floats
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    # Cast to integers if they are floats
    a = int(a)
    b = int(b)

    return a + b
