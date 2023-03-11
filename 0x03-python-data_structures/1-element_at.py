#!/usr/bin/python3

def element_at(my_list, idx):
    for n in my_list:
        if idx == my_list.index(n):
            return n
        elif idx > len(my_list):
            return None
        elif idx < 0:
            return None
