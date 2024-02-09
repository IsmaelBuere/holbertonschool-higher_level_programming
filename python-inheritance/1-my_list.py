#!/usr/bin/python3
"""
In this module, the class MyList is defined.
"""


class MyList(list):
    def print_sorted(self):
        """
        Prints the list elements sorted in ascending order.
        """
        sorted_list = sorted(self)
        print(sorted_list)
