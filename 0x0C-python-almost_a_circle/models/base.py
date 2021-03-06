#!/usr/bin/python3
"""
    Class Base
"""
import json

import os.path


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
        """Method to return a json representation"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """My Funtion to returns python representation of json"""
        if json_string is None:
            return []
        represent = json.loads(json_string)
        return represent

    @classmethod
    def save_to_file(cls, list_objs):
        """Method to save a json file"""
        mylist = []
        filename = f"{cls.__name__}.json"

        if list_objs is not None:
            for objs in list_objs:
                mylist.append(cls.to_dictionary(objs))
        with open(filename, "w", encoding="utf-8") as file:
            file.write(cls.to_json_string(mylist))

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set"""
        if cls.__name__ == "Rectangle":
            dummy = cls(2, 2)
            dummy.update(**dictionary)
        if cls.__name__ == "Square":
            dummy = cls(5)
            dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Load from a json file to convert an object"""
        filename = f"{cls.__name__}.json"
        _object = []
        if os.path.exists(filename):
            with open(filename, "r", encoding="utf-8") as file:
                read = file.read()
                obj = cls.from_json_string(read)
                for ob in obj:
                    _object.append(cls.create(**ob))
        return _object

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Method to save a json file"""
        mylist = []
        filename = f"{cls.__name__}.csv"

        if list_objs is not None:
            for objs in list_objs:
                mylist.append(cls.to_dictionary(objs))
        with open(filename, "w", encoding="utf-8") as file:
            file.write(cls.to_json_string(mylist))

    @classmethod
    def load_from_file_csv(cls):
        """Load from a json file to convert an object"""
        filename = f"{cls.__name__}.csv"
        _object = []
        if os.path.exists(filename):
            with open(filename, "r", encoding="utf-8") as file:
                read = file.read()
                obj = cls.from_json_string(read)
                for ob in obj:
                    _object.append(cls.create(**ob))
        return _object
