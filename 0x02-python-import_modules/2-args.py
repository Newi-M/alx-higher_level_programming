#!/usr/bin/python3
if __name__ == "__main__":   
    import sys

    l = len(sys.argv) 
    if  l == 1:
        print("0 arguments.")
    elif l == 2:
        print("1 argument:")
    else:
        print("{} arguments:".format(l - 1))
    
    for i in range(l - 1):
        print("{}: {}".format(i + 1, sys.argv[i + 1]))
