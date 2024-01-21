#!/usr/bin/python3
import sys

if __name__ == "__main__":

    l = len(sys.argv)
    if l == 2:
        print("1 argument:")
    elif l == 1:
        print("0 arguments.")
        sys.exit()
    else:
        print("{} arguments:".format(l - 1))
    
    for i in range(l):
        print("{}: {}".format(i + 1, sys.argv[i + 1]))
