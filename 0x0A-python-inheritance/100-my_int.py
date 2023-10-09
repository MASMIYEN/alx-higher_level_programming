#!/usr/bin/python3
"""Defines class MyInt"""


class MyInt(int):
    """defines rebel int"""

    def __init__(self, value):
        """initializes new instance"""
        self.__value = value

    def __eq__(self, other):
        """inverts != to =="""
        return self.__value != other

    def __ne__(self, other):
        """inverts == to !="""
        return self.__value == other
