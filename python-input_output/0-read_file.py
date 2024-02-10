#!/usr/bin/python3
"""
Read and print the content of a text file.
"""


def read_file(filename=""):
    """
    Reads a text file (UTF8) and prints it to stdout.
    """
    with open(filename, encoding='utf-8') as file:
        for line in file:
            print(line, end='')
