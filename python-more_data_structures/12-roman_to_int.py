#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str):
        return 0

    roman_numerals = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
    values = [1, 5, 10, 50, 100, 500, 1000]
    integer = 0
    previous_value = 0

    for numeral in reversed(roman_string):
        value = values[roman_numerals.index(numeral)]

        if value < previous_value:
            integer -= value
        else:
            integer += value
            previous_value = value

    return integer
