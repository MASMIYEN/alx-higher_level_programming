#!/usr/bin/python3
"""Define rectangle class"""


class Rectangle:
    """Rectangle class
    Public class attribute number_of_instances
    Public class attribute print_symbol used as
    symbol for string representation
    """

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """initiation method for rectangle class"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """getter returns width"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets width value"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """getter returns height"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets height value"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """returns rectangle area"""
        return self.__width * self.__height

    def perimeter(self):
        """returns rectangle perimeter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return (2 * self.__width) + (2 * self.__height)

    def __str__(self):
        """returns rectangle in #"""
        string = ""
        if self.__width == 0 or self.__height == 0:
            return string
        for i in range(0, self.__height):
            for j in range(0, self.__width):
                string += str(self.print_symbol)
            if i != self.__height - 1:
                string += '\n'
        return string

    def __repr__(self):
        """returns str repr to create new instance"""
        string = "Rectangle("
        string += str(self.__width)
        string += ", " + str(self.__height) + ")"
        return string

    def __del__(self):
        """prints message when instance of rectangle is deleted"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """returns biggest rectangle based on area"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        area1 = rect_1.area()
        area2 = rect_2.area()

        if area1 >= area2:
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """returns new instance with width == height == size"""
        return Rectangle(size, size)
