#!/usr/bin/python
"""Module for the base class"""
from json import dumps, loads
import csv

from pynvim import encoding


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

    @classmethod
    def save_to_file(cls, list_objs):
        """save object in JSON format to a file"""
        if list_objs is not None:
            list_objs = [obj.to_dictionary() for obj in list_objs]
        with open("{}.json".format(cls.__name__), "w", encoding="utf-8") as file:
            file.write(cls.to_json_string(list_objs))
