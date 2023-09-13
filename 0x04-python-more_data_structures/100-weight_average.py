#!/usr/bin/python3
def weight_average(my_list=[]):
    result = 0
    weight = 0
    if my_list:
        for s, w in my_list:
            result += s * w
            weight += w
        result = result / weight
    return result
