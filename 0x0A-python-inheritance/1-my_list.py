#!/usr/bin/python3
"""
    Public instance method: def print_sorted(self):
    that prints the list, but sorted (ascending sort)
"""


class MyList(list):
    """
        Mylist Class
    """
    def __init__(self):
        super().__init__(self)

    def print_sorted(self):
        print(sorted(self))
