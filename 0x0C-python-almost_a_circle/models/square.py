#!/usr/bin/python3
"""Square's class module"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square's class"""

    def __init__(self, size, x=0, y=0, id=None):
        """construct"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return '[{}] ({}) {}/{} - {}'. \
            format(type(self).__name__, self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """size of square"""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def __update(self, id=None, size=None, x=None, y=None):
        """private method to update instances via */**args"""
        if id is not None:
            self.id = id
        if size is not None:
            self.size = size
        if x is not None:
            self.x = x
        if y is not None:
            self.y = y

    def update(self, *args, **kwargs):
        """update instances via no keyword && args keyword"""
        if args:
            self.__update(*args)
        elif kwargs:
            self.__update(**kwargs)
