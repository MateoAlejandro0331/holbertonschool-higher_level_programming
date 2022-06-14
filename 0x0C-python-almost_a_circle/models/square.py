#!/usr/bin/python3
"""
    Class Rectangle that inherits from Base
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
        Class methods
    """
    def __init__(self, size, x=0, y=0, id=None):
        """Constructor Method"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        if len(args) > 0:
            self.id = args[0]
        if len(args) > 1:
            self.width = args[1]
        if len(args) > 2:
            self.x = args[2]
        if len(args) > 3:
            self.y = args[3]
        if args is None or len(args) == 0:
            for key, value in kwargs.items():
                for key1, value1 in self.__dict__.items():
                    if key == key1:
                        setattr(self, key1, value)
                    if "_Rectangle__"+key == key1:
                        setattr(self, key1, value)
                    if key == "size":
                        self.width = value

    def to_dictionary(self):
        return {
                "id": self.id,
                "size": self.width,
                "x": self.x,
                "y": self.y
                }

    def __str__(self):
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"
