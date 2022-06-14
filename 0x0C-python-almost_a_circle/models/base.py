#!/usr/bin/python3
"""
    Class Base
"""
import json


class Base:
    """
        Class Methods
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Constructor Method"""
        if id is None:
            Base.__nb_objects += 1
            self.id = self.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        mylist = []
        if str(cls) == "<class 'models.rectangle.Rectangle'>":
            filename = "Rectangle.json"
        if str(cls) == "<class 'models.square.Square'":
            filename = "Square.json"
        if list_objs is None:
            with open(filename, 'w', encoding='utf-8') as file:
                represent = json.dumps(mylist)
                file.write(represent)
        else:
            with open(filename, 'r+', encoding='utf-8') as file:
                mylist = json.load(file)
