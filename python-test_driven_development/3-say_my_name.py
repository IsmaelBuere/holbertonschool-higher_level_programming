#!/usr/bin/python3
"""
Print the name and lastname
"""


def say_my_name(first_name, last_name=""):
    """
    Prints a formatted message with the provided first and last names.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    
    print(f"My name is {first_name} {last_name}")
