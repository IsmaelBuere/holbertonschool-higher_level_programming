#!/usr/bin/python3
"""
Design two mixin classes
"""


class SwimMixin:
    """
    A mixin class called SwimMixin with a method
    swim that prints The creature swims.
    """

    def swim(self):
        print("The creature swims!")


class FlyMixin:
    """
    A mixin class called FlyMixin with a method
    fly that prints The creature flies.
    """

    def fly(self):
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """
    A class named Dragon that inherits from both SwimMixin and FlyMixin.
    """

    def roar(self):
        print("The dragon roars!")
