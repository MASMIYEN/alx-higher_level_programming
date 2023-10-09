#!/usr/bin/python3
"""Defines class Square inherited from Rectangle class"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Class square definition"""

    def __init__(self, size):
        """initializing square instance"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """returns area of square"""
        return self.__size ** 2

    def __str__(self):
        """returns square description"""
        return "[Square] {:d}/{:d}".format(self.__size, self.__size)
