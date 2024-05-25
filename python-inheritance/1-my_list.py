#!/usr/bin/python3
"""
Write a class MyList that inherits from list
"""


class MyList(list):
        """
        Prints the list in ascending order.
        """
    def print_sorted(self):
        sorted_list = sorted(self)
        print(sorted_list)
