#!/usr/bin/python3
"""
Write a class BaseGeometry with methods area and integer_validator.
"""


class BaseGeometry:
    """
    A class named BaseGeometry with methods to validate geometry values.
    """
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
