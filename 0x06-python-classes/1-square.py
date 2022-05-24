#!/usr/bin/python3
"""My Squere Class"""


class Square:
    """Size private atribute"""
    def __init__(self, num):
        self.size = num
    
    @property
    def num(self):
        return self.__size
