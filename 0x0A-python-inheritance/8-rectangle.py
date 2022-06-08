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
