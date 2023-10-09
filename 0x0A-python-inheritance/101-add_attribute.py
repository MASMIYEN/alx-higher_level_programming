#!/usr/bin/python3
"""defines function that adds new attribute to an object"""


def add_attribute(obj, name, value):
    """adds new attribute to object"""
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, name, value)
