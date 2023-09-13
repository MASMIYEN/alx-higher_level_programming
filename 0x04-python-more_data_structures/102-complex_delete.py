#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    for key, val in list(a_dictionary.items()):
        if val == value:
            a_dictionary.pop(key)
    return a_dictionary
