#!/usr/bin/python3
import random

number = random.randint(-10000, 10000)
last_digit_raw = number % 10 if number >= 0 else number % -10
string = ""

if last_digit_raw > 5:
    string = "and is greater than 5"
elif last_digit_raw < 6 and last_digit_raw != 0:
    string = "and is less than 6 and not 0"
elif last_digit_raw == 0:
    string = "and is 0"

print(f"Last digit of {number} is {last_digit_raw} {string}")
