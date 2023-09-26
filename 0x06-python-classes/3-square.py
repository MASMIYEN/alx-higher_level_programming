#!/usr/bin/python3
"""square"""


class Square:
    """define square"""

    def __init__(self, size=0):
        """construct
        Args:
            size: length of square
        Raises:
            TypeError: if size is no integer
            ValueError: if size is less than zero
        """
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size

    def area(self):
        """Area of square.
        Returns:
            the square of size
        """
        return self.__size ** 2
