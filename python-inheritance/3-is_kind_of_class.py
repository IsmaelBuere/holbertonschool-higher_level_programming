#!/usr/bin/python3
"""
Checks if obj is an instance or subclass.
"""


def is_kind_of_class(obj, a_class):
    """
    Checks if the object is an instance of,
    or if the object is an instance of a class
    that inherited from, the specified class.
    """
    return isinstance(obj, a_class)
