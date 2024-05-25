#!/usr/bin/python3
"""
Write a function that returns True
"""


def inherits_from(obj, a_class):
    """
    Returns True if the object is an instance of
    a class that inherited (directly or indirectly)
    """
    return isinstance(obj, a_class) and type(obj) != a_class
