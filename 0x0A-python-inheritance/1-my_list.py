#!/usr/bin/python3
"""MyList class"""


class MyList(list):
    """subclass of list"""
    def __init__(self):
        """initialization"""
        super().__init__()

    def print_sorted(self):
        """prints the sorted list"""
        print(sorted(self))
