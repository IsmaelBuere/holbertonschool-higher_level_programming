#!/usr/bin/python3
"""
Create a class BaseGeometry.
"""


class BaseGeometry:
    """
    A base class for geometric operations.

    This class serves as a base for implementing geometric operations.
    """
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
