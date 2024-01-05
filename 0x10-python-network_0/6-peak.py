#!/bin/bash/python3
""" module doc """


def find_peak(list_of_integers):
    """ doc def"""
    if list_of_integers:
        lf = 0
        r = len(list_of_integers) - 1
        while lf < r:
            m = (lf + r) // 2
            if list_of_integers[m] < list_of_integers[m + 1]:
                lf = m + 1
            else:
                r = m

        return list_of_integers[lf]
