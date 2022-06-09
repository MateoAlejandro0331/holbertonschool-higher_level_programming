#!/usr/bin/python3
"""
    My class
"""


class Student:
    """Constructor Method"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        mydict = {}
        if attrs is None:
            return vars(self)
        for key, value in self.__dict__.items():
            if key in attrs:
                mydict.setdefault(key, value)
        return mydict
        
