#!/usr/bin/python3
for j in (122, 96, -1):
    if (j % 2) == 0:
        i = 0
    else:
        i = 32
    print("{}".format(chr(j - i)), end="")
