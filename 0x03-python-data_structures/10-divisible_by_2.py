#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if my_list is None:
        return None
    divby2 = []
    for i in my_list:
        if (i % 2) == 0:
            divby2.append(True)
        else:
            divby2.append(False)
    return divby2
