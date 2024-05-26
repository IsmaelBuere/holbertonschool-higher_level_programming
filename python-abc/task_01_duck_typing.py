#!/usr/bin/python3
"""
Create an abstract classes
"""


from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """
    An abstract base class named Shape.
    """

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Circle(Shape):
    """
    A class named Circle that inherits from Shape.
    """

    def __init__(self, radius):
        if radius <= 0:
            raise ValueError("Radius must be a positive number")
        self.__radius = radius

    def area(self):
        return math.pi * (self.__radius ** 2)

    def perimeter(self):
        return 2 * math.pi * self.__radius


class Rectangle(Shape):
    """
    A class named Rectangle that inherits from Shape.
    """

    def __init__(self, width, height):
        self.__width = width
        self.__height = height

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        return 2 * (self.__width + self.__height)


def shape_info(shape):
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")
