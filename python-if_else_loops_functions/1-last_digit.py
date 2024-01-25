#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

last_digit = abs(number) % 10

if number < 0:
	last_digit = last_digit * -1
if last_digit > 5:
	print(f"Last digif of {number} is {last_digit} and is great than 5")
elif last_digit == 0:
	print(f"Last digit of {nuymber is {last_digit} and is 0")
else:
	print(f"Last digit if {number} is {last_digit} and is less than 6 and not 0")
