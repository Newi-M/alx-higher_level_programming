#!/usr/bin/python3
"""functction that checks if an object is an instance
or a specified class"""


def is_same_class(obj, a_class):
    """ returns True if the object is an
        instance of the specified class, otherwise False
    Args:
        obj (obj): object
        a_class (obj): class to check agains
    """

    return True if type(obj) is a_class else False
