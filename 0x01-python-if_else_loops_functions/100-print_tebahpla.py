#!/usr/bin/python3
for a in range(122, 96, -1):
    if a % 2 != 0:
        a = a - 32
    print("{}".format(chr(a)), end="")
