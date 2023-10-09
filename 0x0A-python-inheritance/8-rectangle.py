#!/usr/bin/python3
"""Define class rectangle that inherits from BaseGeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ define class rectangle """

    def __init__(self, width, height):
        """initializing rectangle instance"""
        self.integer_validator("width", width)
        self._width = width
        self.integer_validator("height", height)
        self._height = height
