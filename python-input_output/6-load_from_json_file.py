#!/usr/bin/python3
"""
Write a function that creates an Object
"""
import json


def load_from_json_file(filename):
    """
    Function : load_from_json_file is creating an object
    """
    with open(filename, "r", encoding="UTF-8") as f:
        return json.load(f)
