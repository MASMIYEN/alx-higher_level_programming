#!/usr/bin/python3
"""square"""


class Square:
    """define square"""

    def __init__(self, size=0):
        """construct
        Args:
            size: length of square
        """
        self.size = size

    @property
    def size(self):
        """ length of a side of the square
        Raises:
            TypeError: is size is not an integer
            ValueError: if size is less than zero
        """
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        """Area of the square
        Returns:
            The size squared
        """
        return self.__size ** 2

    def my_print(self):
        """print the square"""
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end="")
                print()