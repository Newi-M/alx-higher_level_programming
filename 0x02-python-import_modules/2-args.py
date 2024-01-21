#!/usr/bin/python3
if __name__ == "__main__":

    l = len(argv)
    for i in range(l):
        if l == 1:
            print("1 argument:")
        else:
            print("{} arguments:".format(i))
        print("{}: {}".format(i + 1, argv[i])
