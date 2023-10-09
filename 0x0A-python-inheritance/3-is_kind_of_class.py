#!/usr/bin/python3
"""defines function is_kind_of_class"""


def is_kind_of_class(obj, a_class):
    """return True if obj is instance or inherited from a_class"""
    return isinstance(obj, a_class)
