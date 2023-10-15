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
