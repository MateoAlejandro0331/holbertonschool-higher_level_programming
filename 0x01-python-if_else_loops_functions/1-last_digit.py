#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lastn = number % 10 
if lastn > 5:
    print(f"Last digit of {lastn} and is greater than 5")
elif lastn == 0:
    print(f"Last digit of {lastn} and is 0")
elif lastn < 6:
    print(f"Last digit of {lastn} and is less than 6 and not 0")

