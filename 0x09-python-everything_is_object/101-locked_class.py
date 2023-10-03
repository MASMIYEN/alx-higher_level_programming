#!/usr/bin/python3
"""
Define LockedClass class
"""


class LockedClass:
    """
    prevent the user from creating new instance attribute
    except for first_name
    """
    __slots__ = ["first_name"]

    def __init__(self):
        """
        create new instance in LockedClass
        """
        self.first_name = "first_name"
