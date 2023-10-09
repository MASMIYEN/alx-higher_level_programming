#!/usr/bin/python3
"""Defines function that prints a square with #"""


def print_square(size):
    """prints square in #"""
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        for j in range(size):
            print('#', end="")
        print("")
