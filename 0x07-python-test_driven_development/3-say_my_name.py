#!/usr/bin/python3
"""

Funtion to concatenate two strings

"""


def say_my_name(first_name, last_name=""):
    """
    vereficate all the posible cases
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print(f"My name is {first_name} {last_name}")
