#!/usr/bin/python3
""" define a rectangle class inherited from BaseGeometry"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """define rectangle class"""

    def __init__(self, width, height):
        """initializing rectangle instances"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """ returning area of rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """return description for the rectangle"""
        string = "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)
        return string
