#!/usr/bin/python3
"""Import the class"""
from curses.textpad import rectangle


Rectangle = __import__('8-rectangle').Rectangle
"""
    Class Rectangle that inherits from BaseGeometry
"""

class Square(Rectangle):
    """
        My class
    """
    def __init__(self, size):
        """Constructor method"""
        super().integer_validator("size", size)
        self.__size = size

    def area(self):
        return self.__size * self.__size

    def __str__(self):
        return f"[Rectangle] {self.__size}/{self.__size}"
