#!/usr/bin/python3
"""
Defines a Rectangle class.
"""
from models.base import Base


class Rectangle(Base):
    """Represent a rectangle."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initialize a new Rectangle.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Get/set the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the rectangle."""
        self.__width = value

    @property
    def height(self):
        """Get/set the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the rectangle."""
        self.__height = value

    @property
    def x(self):
        """Get/set the x coordinate of the rectangle's position."""
        return self.__x

    @x.setter
    def x(self, value):
        """Set the x coordinate of the rectangle's position."""
        self.__x = value

    @property
    def y(self):
        """Get/set the y coordinate of the rectangle's position."""
        return self.__y

    @y.setter
    def y(self, value):
        """Set the y coordinate of the rectangle's position."""
        self.__y = value

    def area(self):
        """Compute the area of the rectangle."""
        return self.width * self.height

    def display(self):
        """Display the rectangle."""
        for _ in range(self.y):
            print()
        for _ in range(self.height):
            print(" " * self.x + "#" * self.width)

    def __str__(self):
        """Return the string representation of the rectangle."""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        """Update the rectangle's attributes."""
        if args:
            attrs = ['id', 'width', 'height', 'x', 'y']
            for attr, value in zip(attrs, args):
                setattr(self, attr, value)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Return a dictionary representation of the rectangle."""
        return {'id': self.id, 'width': self.width, 'height': self.height,
                'x': self.x, 'y': self.y}
