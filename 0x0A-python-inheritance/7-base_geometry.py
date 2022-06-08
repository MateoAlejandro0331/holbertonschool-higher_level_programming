#!/usr/bin/python3
"""
    Class BaseGeometry.
"""


class BaseGeometry:
    """
        My class
    """

    def area(self):
        """Method not defined"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
