#!/usr/bin/python3
i = 1
for j in (122, 96, -1):
    if (i % 2) == 0:
        print("{}".format(chr(j - 32)), end="")
        i = i + 1
    else:
        print("{}".format(chr(j)), end="")
