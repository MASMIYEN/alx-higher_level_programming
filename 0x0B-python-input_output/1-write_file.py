#!/usr/bin/python3
"""write file with 2 args definition"""


def write_file(filename="", text=""):
    """read filename with utf-8 encoding"""
    with open(filename, "w", encoding='utf-8') as file:
        return file.write(text)
