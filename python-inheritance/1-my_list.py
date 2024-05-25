#!/usr/bin/python3
"""
This module provides utilities for inspecting Python objects.
"""


class MyList(list):
    """
    A subclass of list
    """
    def print_sorted(self):
        print(sorted(self))
