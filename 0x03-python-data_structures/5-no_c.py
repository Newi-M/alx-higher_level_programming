#!/usr/bin/python3
def no_c(my_string):
    c_no_str = my_string.translate({ord('c'): None})
    c_no_str = c_no_str.translate({ord('C'): None})
    return c_no_str
