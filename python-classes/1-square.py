#!/usr/bin/python3
"""
This is the module docstring. This module contains a definition of a Square.
"""


class Square:
    """
    A class that defines a square.
    Attributes:
    - __size (int): Private instance attribute
    representing the size of the square.
    """
    def __init__(self, size):
        """
        Initializes an instance of the Square class with a given size.
        Parameters:
        - size (int): The size of the square.
        """
        self.__size = size
