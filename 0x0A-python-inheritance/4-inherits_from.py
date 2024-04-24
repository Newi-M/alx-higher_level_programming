#!/usr/bin/python3
"""Defines inherited class-checking function."""


def inherits_from(obj, a_class):
    """Checks if an object is an inherited instance.

    Args:
        obj (any): object
        a_class (type): class to match the type of obj to.
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
