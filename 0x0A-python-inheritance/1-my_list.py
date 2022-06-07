#!/usr/bin/python3
"""
    Public instance method: def print_sorted(self):
    that prints the list, but sorted (ascending sort)
"""


class MyList(list):
    """
        Mylist Class
    """
    def print_sorted(self):
        print(sorted(self))
