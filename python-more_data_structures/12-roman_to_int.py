#!/usr/bin/python3
def roman_to_int(s):
    roman = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
        }
    last, total = 0, 0
    for i in s[::-1]:
        if last == 0:
            last = roman[i]
        if roman[i] < last:
            total -= 2*roman[i]
        total += roman[i]
        last = roman[i]
    return total
