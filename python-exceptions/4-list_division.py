#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    result = []
    try:
        for i in range(list_length):
            try:
                if i >= len(my_list_1) or i >= len(my_list_2):
                    raise IndexError("out of range")
                value_1 = my_list_1[i]
                value_2 = my_list_2[i]
                try:
                    division_result = value_1 / value_2
                    result.append(division_result)
                except ZeroDivisionError:
                    print("division by 0")
                    result.append(0)
            except IndexError:
                print("out of range")
                result.append(0)
            except TypeError:
                print("wrong type")
                result.append(0)
    finally:
        return result
