#!/usr/bin/python3
"""
Write a function that reads a text file
"""


def read_file(filename=""):
    """
    Try to open a file
    """
    try:
        with open(filename, "r", encoding="utf-8") as file:
            print(file.read())
    except:
        pass