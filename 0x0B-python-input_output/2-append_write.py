#!/usr/bin/python3
"""Defines a function that appends a string at the end of a text file"""


def append_write(filename="", text=""):
    """Appends a string to the end of a text file.

    Args:
        filename (str): name of file to append to.
        text (str): string to append to file.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
