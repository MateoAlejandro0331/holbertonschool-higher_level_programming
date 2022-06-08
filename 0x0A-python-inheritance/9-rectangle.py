#!/usr/bin/python3
"""Import the class"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry
"""
    Class Rectangle that inherits from BaseGeometry
"""


class Rectangle(BaseGeometry):
    """
        My class
    """
    def __init__(self, width, height):
        """Method init an super() """
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        return self.__height * self.__width

    def __str__(self):
        return f"[Rectangle] {self.__width}/{self.__height}"
