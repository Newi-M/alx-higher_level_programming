#!/usr/bin/python3
"""determines if an object is an instance of a class"""


def inherits_from(obj, a_class):
    """Returns True if the object is an instance of a class that
    inherited from the specified class, otherwise False.
    Args:
        obj (obj): object
        a_class (obj): class to check against
    """

    return True if isinstance(obj, a_class) and \
        type(obj) is not a_class else False
