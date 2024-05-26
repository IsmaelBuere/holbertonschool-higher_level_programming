#!/usr/bin/python3
"""
Define a class Rectangle that inherits from BaseGeometry.
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Defines a rectangle class
    that inherits from BaseGeometry
    """

    def __init__(self, width, height):
        self.__width = width
        self.__height = height

        self.integer_validator("width", width)
        self.integer_validator("height", height
