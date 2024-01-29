#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    if key in a_dictionary:
        a_dictionary[key] = value
    else:
        a_dictionary[key] = value

my_dictionary = {'a': 1, 'b': 2, 'c': 3}
update_dictionary(my_dictionary, 'b', 10)
update_dictionary(my_dictionary, 'd', 4)
print(my_dictionary)
