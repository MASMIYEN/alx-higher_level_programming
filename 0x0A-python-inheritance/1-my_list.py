#!/usr/bin/python3
"""Defines class MyList that inherits from list"""


class MyList(list):
    """subclass of list"""
    def __init__(self):
        """initializing the object"""
        super().__init__()

    def print_sorted(self):
        """prints the list but sorted"""
        print(sorted(self))
