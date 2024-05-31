#!/usr/bin/python3
"""
Write a class Student that defines a student
"""


class Student:
    def __init__(self, first_name, last_name, age):
        """
        Initialize a new Student instance.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        return {key: value for key, value in self.__dict__.items()
                if isinstance(value, (list, dict, str, int, bool))}

