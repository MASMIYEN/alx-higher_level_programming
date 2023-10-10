#!/usr/bin/python3
"""append file with 2 args definition"""


def append_write(filename="", text=""):
    """append filename with utf-8 encoding"""
    with open(filename, "a", encoding='utf-8') as file:
        return file.write(text)
