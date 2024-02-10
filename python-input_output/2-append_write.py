#!/usr/bin/python3
"""
Append a string at the end of a text file
and return the number of characters added.
"""


def append_write(filename="", text=""):
    """
    Appends a string to the end of a text file (UTF8) and
    returns the number of characters added.
    """
    with open(filename, mode='a', encoding='utf-8') as file:
        file.write(text)
        return len(text)
