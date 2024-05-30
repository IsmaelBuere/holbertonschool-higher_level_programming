#!/usr/bin/python3
"""

"""
def load_from_json_file(filename):
    """
    Function : load_from_json_file is creating an object
    """

    with open(filename, "r", encoding="utf-8") as fic:
        r = json.load(fic)
        return r
