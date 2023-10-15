#!/usr/bin/python
"""Module for the base class"""
from json import dumps, loads
import csv


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """Dictionary to JSON string method"""
        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        else:
            return dumps(list_dictionaries)
