#!/usr/bin/python3
"""
Contains the class BaseGeometry
"""


class BaseGeometry:
    """A class with public attribute area"""

    def area(self):
        """raises an exception when called"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates value if integer type and positive"""
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
