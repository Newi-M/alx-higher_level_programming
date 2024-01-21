#!/usr/bin/python3
if __name__ == "__main__":

    import sys

    l = len(sys.argv)
    for i in range(l):
        if l == 2:
            print("1 argument:")
        elif l == 1:
            print("0 arguments.")
            break
        else:
            print("{} arguments:".format(l - 1))
        print("{}: {}".format(i + 1, sys.argv[i + 1])
