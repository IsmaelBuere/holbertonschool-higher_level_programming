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

    i = 0
    while i < len(text):
        print(text[i], end="")
        if text[i] in ".?:":
            print("\n\n", end="")
            while i + 1 < len(text) and text[i + 1] == ' ':
                i += 1
        i += 1
