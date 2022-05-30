#!/usr/bin/python3
""" 

Functions to add to integers and validations 

"""


def add_integer(a, b=98):
    """
    Functions to add to integers and validations 
    """
    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)
    if type(a) is not int:
        raise TypeError("a must be an integer")
    if type(b) is not int:
        raise TypeError("b must be an integer")
    return a + b
