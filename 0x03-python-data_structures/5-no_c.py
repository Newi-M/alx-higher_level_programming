#!/usr/bin/python3
def no_c(my_string):
    l = list(my_string)
    for n in l:
        if n == 'c':
            l.remove('c')
        if n == 'C':
            l.remove('C')
    my_string = "".join(l)
    return my_string
