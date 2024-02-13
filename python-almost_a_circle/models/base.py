#!/usr/bin/python3
"""Create Class Base"""


class Base:
    """
    A base class that manages the id attribute in all future classes.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
