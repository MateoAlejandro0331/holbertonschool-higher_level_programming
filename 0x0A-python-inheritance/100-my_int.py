#!/usr/bin/python3
"""
    Import the class
"""


class MyInt(int):
    """ My class"""

    def __eq__(self, num):
        return int.__ne__(self, num)

    def __ne__(self, num):
        return int.__eq__(self, num)
