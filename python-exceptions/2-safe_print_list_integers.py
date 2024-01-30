#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count_integers = 0

    try:
        for i in range(x):
            value = my_list[i]
            print("{:d}".format[i], end='')
            count_integers += 1
    except (ValueError, TypeError, IndexError):
        pass
    print()
    return count_integers
