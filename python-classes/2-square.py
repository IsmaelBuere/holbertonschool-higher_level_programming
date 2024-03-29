#!/usr/bin/python3
"""
This is the module docstring. This module contains a definition of a Square.
"""


class Square:
    """
    Square class for representing a square object.
    """

    def __init__(self, size=0):
        self.__size = 0
        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
