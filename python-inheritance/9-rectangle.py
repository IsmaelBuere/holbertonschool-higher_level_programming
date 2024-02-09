#!/usr/bin/python3
"""
Defines a Rectangle class.
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Represents a rectangle.
    """
    def __init__(self, width, height):
        super().__init__()
        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)

    def area(self):
        return self.__width * self.__height

    def __str__(self):
        return "[Rectangle] {}/{}".format(self.__width, self.__height)

if __name__ == "__main__":
    r = Rectangle(3, 5)
    print(r)
    print("Area: {}".format(r.area()))
