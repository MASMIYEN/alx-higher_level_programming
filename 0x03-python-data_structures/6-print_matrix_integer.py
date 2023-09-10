#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix:
        return None
    for neo in matrix:
        if len(neo) == 0:
            print()
        for i in range(len(neo)):
            print("{:d}".format(neo[i]),
                    end="\n" if i is len(neo) - 1 else " ")
