#!/usr/bin/python3
"""
Checks if obj is an instance of a class that inherited
"""


def inherits_from(obj, a_class):
    """
    Checks if the object is an instance of
    a class that inherited (directly or indirectly)
    from the specified class.
    """
    # Get the class of the object
    obj_class = obj.__class__

    while obj_class is not object:
        if obj_class is a_class:
            return True
        obj_class = obj_class.__base__

    return False
