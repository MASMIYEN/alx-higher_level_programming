#!/usr/bin/python3
"""pascal_triangle function"""


def pascal_triangle(n):
    """returns list of lists of ints Pascal triangle"""
    trio = []
    if n <= 0:
        return trio
    for i in range(n):
        for j in range(i + 1):
            if j == 0:
                trio.append([1])
            elif j == i:
                trio[i].append(1)
            else:
                trio[i].append(trio[i - 1][j] + trio[i - 1][j - 1])
    return trio