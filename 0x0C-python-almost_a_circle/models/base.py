#!/usr/bin/python
"""Module for the base class"""


class Base:
    """ Base class representation"""
    __nb_objects = 0

    def __init__(self, id=None):
        """construct"""
        if id is not None:
            self.id = id
        else:  # increment __nb_objects and assign the new value to the public instance attribute id
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
