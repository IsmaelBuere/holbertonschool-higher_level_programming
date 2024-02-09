#!/usr/bin/python3
"""
Returns a list of the available attributes and methods.
"""


def lookup(obj):
    """
    This function returns a list of the attributes
    and methods of the provided object.
    """
    return dir(obj)
