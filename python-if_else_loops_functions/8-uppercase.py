#!/usr/bin/python3
def uppercase(input_str):
    for char in input_str:
        if 97 <= ord(char) <= 122:
            uppercase_char = chr(ord(char) - 32)
            print('{}'.format(uppercase_char), end='')
        else:
            print('{}'.format(char), end='')

    print()
