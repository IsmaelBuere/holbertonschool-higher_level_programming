#!/usr/bin/python3
"""
Create class Student
"""


class Student:
    """
    Defines a Student.
    """

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs is None:
            return self.__dict__
        else:
            return {
                attr: getattr(self, attr)
                for attr in attrs
                if attr in self.__dict__
            }

    def reload_from_json(self, json):
        for key, value in json.items():
            setattr(self, key, value)
