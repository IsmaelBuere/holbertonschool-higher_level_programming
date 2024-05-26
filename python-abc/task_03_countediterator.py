#!/usr/bin/python3
"""
Create a class named CountedIterator
"""


class CountedIterator:
    """
    A class named CountedIterator that extends the built-in iterator obtained from the iter function.
    """

    def __init__(self, iterable):
        self.iterator = iter(iterable)
        self.count = 0

    def __next__(self):
        try:
            item = next(self.iterator)
            self.count += 1
            return item
        except StopIteration:
            raise StopIteration("No more items to iterate over")

    def get_count(self):
        return self.count
