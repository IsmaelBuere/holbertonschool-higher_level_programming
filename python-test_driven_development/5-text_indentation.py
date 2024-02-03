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

    text = text.replace('.', '.\n\n')
    text = text.replace('?', '?\n\n')
    text = text.replace(':', ':\n\n')

    lines = text.split('\n')
    for i in range(len(lines)):
        lines[i] = lines[i].strip()

    text = '\n'.join(lines)
    print(text)
