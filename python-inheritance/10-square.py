#!/usr/bin/python3
"""
Defines a Square class.
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Class that defines a Square from Rectangle class
    """
    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(self.__size, self.__size)

    def area(self):
        return super().area()
