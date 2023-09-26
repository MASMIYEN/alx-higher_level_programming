#!/usr/bin/python3
"""Square"""


class Square:
    """define square"""

    def __init__(self, size=0, position=(0, 0)):
        """initialization function"""
        self.__size = size
        self.__position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """returns area of square"""
        return self.__size ** 2

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if (
                not isinstance(value, tuple)
                or len(value) != 2
                or not all(isinstance(x, int) and x >= 0 for x in value)
        ):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        space = ""
        if self.__size == 0:
            print()
        else:
            for i in range(self.__position[1]):
                space += "\n"
            for i in range(self.__size):
                for j in range(self.__position[0]):
                    space += " "
                for j in range(self.__size):
                    space += "#"
                space += "\n"
            print("{}".format(space), end="")
