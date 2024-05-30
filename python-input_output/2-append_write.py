#!/usr/bin/python3
"""
Write a function that appends a string at the end of a text file
"""


def append_write(filename="", text=""):
    """
    Function that appends a string at the end of a text file
    """
    with open(filename, "a") as fail:
        return fail.write(text)
