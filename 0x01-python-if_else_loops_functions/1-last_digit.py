#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    lastn = (number * -1) % 10
else:
    lastn = number % 10
if lastn > 5:
    print(f"Last digit of {number} is {lastn} and is greater than 5")
elif lastn == 0:
    print(f"Last digit of {number} and is 0")
elif lastn < 6:
    print(f"Last digit of {number} is {lastn} and is less than 6 and not 0")
