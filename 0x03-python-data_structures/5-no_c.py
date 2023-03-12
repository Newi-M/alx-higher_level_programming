#!/usr/bin/python3
def no_c(my_string):
    lists = list(my_string)
    for n in lists:
        if n == 'c':
            lists.remove('c')
        if n == 'C':
            lists.remove('C')
    my_string = "".join(lists)
    return my_string
