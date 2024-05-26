#!/usr/bin/python3
"""
Create an abstract classes
"""


from abc import ABC, abstractmethod

class Animal(ABC):
    """
    Abstract base class for animals.
    """
    @abstractmethod
    def sound(self):
        pass

class Dog(Animal):
    """
    Subclass representing a dog.
    """
    def sound(self):
        return "Bark"

class Cat(Animal):
    """
    Subclass representing a cat.
    """
    def sound(self):
        return "Meow"
