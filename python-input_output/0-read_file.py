#!/usr/bin/python3
"""
Write a function that reads a text file
"""


def read_file(filename=""):
    """
    Try to open a file
    """
    with open(filename, 'r', encoding="utf-8") as fic:
        content = fic.read()
        for f in content:
            print("{}".format(f), end="")