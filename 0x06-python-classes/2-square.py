#!/usr/bin/python3
"""square"""


class Square:
    """define square"""

    def __init__(self, size=0):
        """construct
        Args:
            size: length of square
        raises:
            TypeError: if size not integer
            ValueError: if size is less than zero
        """
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size
