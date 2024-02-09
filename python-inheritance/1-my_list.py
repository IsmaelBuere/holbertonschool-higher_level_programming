#!/usr/bin/python3
"""
In this module, the class MyList is defined.
"""


class MyList(list):
    """
    Prints the list elements sorted in ascending order.
    """
    def print_sorted(self):
        print(sorted(self))
