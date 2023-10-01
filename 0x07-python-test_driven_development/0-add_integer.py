#!/usr/bin/python3
"""Add integer module"""


def add_integer(a, b=98):
    """Add two integers

    Args:
        a:1st integer
        b:2nd integer, 98 as default value

    Raises:
        TypeError:if a and b aren't integers, floats

    Returns:
        sum of the two integers
    """

    if type(a) not in (int, float):
        raise TypeError('a must be an integer')
    if type(b) not in (int, float):
        raise TypeError('b must be an integer')
    return int(a) + int(b)


if __name__ == "__main__":
    import doctest

    doctest.testfile("test/0-add_integer.txt")
