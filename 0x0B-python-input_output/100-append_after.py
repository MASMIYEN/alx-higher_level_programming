#!/usr/bin/python3
"""Module with append_after function"""


def append_after(filename="", search_string="", new_string=""):
    """inserts line of text to a file after specific string"""
    with open(filename, "r") as myFile:
        reader = myFile.readlines()
    with open(filename, "w") as modFile:
        words = ""
        for l in reader:
            words += l
            if search_string in l:
                words += new_string
        modFile.write(words)
