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

    lines = []
    line = ""
    for char in text:
        line += char
        if char in ".?:":
            lines.append(line.strip())
            line = ""
    if line:
        lines.append(line.strip())

    for line in lines:
        print(line + "\n")
