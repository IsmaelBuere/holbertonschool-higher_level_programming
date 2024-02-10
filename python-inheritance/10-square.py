#!/usr/bin/python3
"""
Defines a Square class.
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Represents a square, inherits from Rectangle.
    """
    def __init__(self, size):
        super().__init__(size, size)
        self.__size = size
        self.integer_validator("size", size)

    def area(self):
        return super().area()
