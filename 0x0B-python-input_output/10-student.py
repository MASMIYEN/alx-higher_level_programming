#!/usr/bin/python3
"""task 10 """


class Student:
    """student class"""

    def __init__(self, first_name, last_name, age):
        """student obj"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ return dictionary of a student instance
        if attrs are list of strings
        all attr must be retrieved
        """
        try:
            for attr in attrs:
                if type(attr) is not str:
                    return self.__dict__
        except Exception:
            return self.__dict__
        my_dict = dict()
        for key, value in self.__dict__.items():
            if key in attrs:
                my_dict[key] = value
        return my_dict
