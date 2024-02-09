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
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))