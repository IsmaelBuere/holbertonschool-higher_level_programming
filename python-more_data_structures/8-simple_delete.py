#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):

    if key in a_dictionary:
        del a_dictionary[key]
my_dictionary = {'a': 1, 'b': 2, 'c': 3}
simple_delete(my_dictionary, 'b')
simple_delete(my_dictionary, 'd')
print(my_dictionary)
