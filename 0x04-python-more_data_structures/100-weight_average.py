#!/usr/bin/python3

def weight_average(my_list=[]):
    sum = 0
    i = 0
    if my_list == []:
        return 0
    for j in my_list:
        sum += j[0] * j[1]
        i += j[1]
    return sum/i
