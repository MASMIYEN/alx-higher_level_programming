#!/usr/bin/python3
def remove_char_at(str, n):

    if n >= 0:
        cpy = str[0:n] + str[n + 1:]
        return cpy
    else:
        return str
