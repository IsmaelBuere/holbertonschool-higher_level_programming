#!/usr/bin/python3
"""
Create a class named VerboseList
"""


class VerboseList(list):
    """
    A class named VerboseList that extends the Python list class.
    """

    def append(self, item):
        super().append(item)
        print(f"Added {item} to the list.")

    def extend(self, iterable):
        super().extend(iterable)
        count = len(iterable)
        print(f"Extended the list with {count} items.")

    def remove(self, item):
        print(f"Removed {item} from the list.")
        super().remove(item)

    def pop(self, index=-1):
        item = super().pop(index)
        print(f"Popped {item} from the list.")
        return item