#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last = int(str(number)[-1]) 
if number < 0:
    last = last * -1
string = ""
if last > 5:
    string = "and is greater than 5"
elif last < 6:
    string = "and is less than 6 and not 0"
else:
    string = "and is 0"
print(f"Last digit of {number} is {last} {string}") 
