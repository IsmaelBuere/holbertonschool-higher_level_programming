#!/usr/bin/python3
def print_last_digit(number):
    last_number = abs(number) % 10
    print(last_number, end="", flush=True)
    return last_number
