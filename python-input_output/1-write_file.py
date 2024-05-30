#!/usr/bin/python3
"""
Write a function that writes a string to a text file
"""


def write_file(filename="", text=""):
    """
    Function that writes a string to a text file
    """
    with open(filename, "w") as file:
        return file.write(text)
