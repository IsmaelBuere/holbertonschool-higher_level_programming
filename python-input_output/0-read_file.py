#!/usr/bin/python3
"""
Write a function that reads a text file
"""


def read_file(filename=""):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            print(file.read())
    except:
        pass