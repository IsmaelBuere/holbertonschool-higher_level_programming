#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    result_dict = {}
    for key, value in a_dictionary.items():
        new_value = value * 2
        result_dict[key] = new_value
    return result_dict
