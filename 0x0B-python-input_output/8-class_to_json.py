#!/usr/bin/python3
"""class_to_json()"""


def class_to_json(obj):
    """Returns dictionary description with simple data structure"""
    return obj.__dict__
