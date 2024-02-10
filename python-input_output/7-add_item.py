#!/usr/bin/python3
"""
Script that adds all arguments to a Python list.
"""


import sys


from save_to_json_file import save_to_json_file
from load_from_json_file import load_from_json_file

try:
    data = load_from_json_file("add_item.json")
except FileNotFoundError:
    data = []

data.extend(sys.argv[1:])

save_to_json_file(data, "add_item.json")
