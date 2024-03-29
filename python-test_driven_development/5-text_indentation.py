#!/usr/bin/python3
"""
Contains method that prints text with 2 new lines after each ".", "?", and ":"
"""


def text_indentation(text):
    """
    Prints the provided text with additional line breaks after
    periods ('.'), question marks ('?'), and colons (':').
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for char in ".?:":
        text = text.replace(char, char + "\n\n")
    list_lines = [lines.strip(' ') for lines in text.split('\n')]
    revised = "\n".join(list_lines)
    print(revised, end="")
