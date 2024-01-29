#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    a_dictionary.pop(key, None)
my_dictionary = {'a': 1, 'b': 2, 'c': 3}
simple_delete(my_dictionary, 'b')
simple_delete(my_dictionary, 'd')

print(my_dictionary)
