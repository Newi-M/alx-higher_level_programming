#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return "None"
    else:
        biggest_element = my_list[0]
        for i in range(len(my_list)):
            if my_list[i] > biggest_element:
                biggest_element = my_list[i]
        return biggest_element
