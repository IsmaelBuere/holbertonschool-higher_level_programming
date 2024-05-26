#!/usr/bin/python3
"""
Write a class Rectangle that inherits from BaseGeometry
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class"""

    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__heigth = height

    def area(self):
        return self.__width * self.__heigth

    def __str__(self):
        return str(f"[Rectangle] {self.__width}/{self.__heigth}")
