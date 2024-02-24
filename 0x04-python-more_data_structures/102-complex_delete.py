#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    newlist = []
    if value in a_dictionary.values():
        for key, i in a_dictionary.items():
            if value == i:
                newlist.append(key)

        for j in newlist:
            if j in a_dictionary:
                del a_dictionary[j]
    return a_dictionary
