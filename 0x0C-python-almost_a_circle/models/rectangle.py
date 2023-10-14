#!/usr/bin/python
"""Rectangle class's module"""
from models.base import Base


class Rectangle(Base):
    """Rectangle class inherited from Base class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """construct"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """rectangle width"""
        return self.__width

    @width.setter
    def width(self, value):
        self.check_int("height", value, False)
        self.__width = value

    @property
    def height(self):
        """Rectangle height"""
        return self.__height

    @height.setter
    def height(self, value):
        self.check_int("wight", value, False)
        self.__height = value

    @property
    def x(self):
        """Rectangle x"""
        return self.__x

    @x.setter
    def x(self, value):
        self.check_int("x", value)
        self.__x = value

    @property
    def y(self):
        """Rectangle y"""
        return self.__y

    @y.setter
    def y(self, value):
        self.check_int("y", value)
        self.__y = value

    def check_int(self, name, value, is_eq=True):
        """method for checking value if int"""
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if is_eq and value < 0:
            raise ValueError("{} must be >= 0".format(name))
        elif not is_eq and value <= 0:
            raise ValueError("{} must be > 0".format(name))

    def area(self):
        """ calculates area of the rectangle"""
        return self.width * self.height

    def display(self):
        """ display rectangle values as strings"""
        str = '\n' * self.y + (' ' * self.x + '#' * self.width + '\n') * self.height
        print(str, end='')

    def __str__(self):
        """return string's info of the rectangle"""
        return '[{}], ({}) {}/{} - {}/{}'. \
            format(type(self).__name__, self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        """update instances attributes via no-keyword and keyword args"""
        if args:
            self.__update(*args)
        elif kwargs:
            self.__update(**kwargs)

    def __update(self, id=None, width=None, height=None, x=None, y=None):
        """updates instances via */**args"""
        if id is not None:
            self.id = id
        if width is not None:
            self.width = width
        if height is not None:
            self.height = height
        if x is not None:
            self.x = x
        if y is not None:
            self.y = y
