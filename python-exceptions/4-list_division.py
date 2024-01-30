#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result_list = []

    for i in range(list_length):
        try:
            result = my_list_1[i] / my_list_2[i]
        except TypeError:
            print("wrong type")
            return 0
        except ZeroDivisionError:
            print("division by 0")
            return 0
        except IndexError:
            print("out of range")
            return 0
        finally:
            result_list.append(result)
    return (result_list)
