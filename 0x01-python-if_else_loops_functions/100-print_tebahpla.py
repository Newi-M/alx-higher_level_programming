#!/usr/bin/python3
i = 1
for j in (122, 96):
    if (i % 2) == 0:
        print(chr(j - 32), end="")
        i = i + 1
    else:
        print(chr(j), end="")
    j = j - 1
