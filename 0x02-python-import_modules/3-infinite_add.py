#!/usr/bin/python3

import sys

l = len(sys.argv)
sum = 0
if __name__ == "__main__":
    if l == 1:
        sum = 0
    else:
        for i in range(1, l):
            sum += int(sys.argv[i])
    print("{}".format(sum))
