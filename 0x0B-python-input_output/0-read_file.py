#!/usr/bin/python3
"""read_file definition """


def read_file(filename=""):
    """reads file with utf-8 encoding"""
    with open(filename, encoding='utf-8') as file:
        print(file.read(), end="")
