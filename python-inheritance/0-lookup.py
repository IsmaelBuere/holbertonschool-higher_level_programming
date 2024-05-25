#!/usr/bin/python3
"""
Write a function that returns a list
"""


def lookup(obj):
    """
    Returns the list of available attributes and methods of an object.
    """
    return dir(obj)
