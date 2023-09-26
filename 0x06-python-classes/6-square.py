#!/usr/bin/python3
"""square"""


class Square:
    """define square"""

    def __init__(self, size=0, position=(0, 0)):
        """construct
        Args:
            size: length of square
        """
        self.size = size
        self.position = position

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
        elif value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    @property
    def position(self):
        """get the current position"""
        return self.__position

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

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
