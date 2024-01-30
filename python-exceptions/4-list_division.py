#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result_list = []

    try:
        for i in range(list_length):
            element1 = my_list_1[i] if i < len(my_list_1) else 0
            element2 = my_list_2[i] if i < len(my_list_2) else 0
            result = element1 / element2 if element2 != 0 else 0
            result_list.append(result)

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
        return result_list
