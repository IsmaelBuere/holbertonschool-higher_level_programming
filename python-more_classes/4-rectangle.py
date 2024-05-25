#!/usr/bin/python3
'''
Square class
'''


class Rectangle:
    """Represents a rectangle."""

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if isinstance(value, int) is False:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if isinstance(value, int) is False:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        return 2 * (self.__width + self.__height)

    def __str__(self):
        message = ""
        if self.__width == 0 or self.__height == 0:
            return message
        else:
            for i in range(self.__height):
                for j in range(self.__width):
                    message += "#"
                if i != self.__height - 1:
                    message += "\n"
        return message

    def __repr__(self):
        return f"Rectangle({self.__width}, {self.__height})"
        
    def __del__(self):
        print("Bye rectangle...")
