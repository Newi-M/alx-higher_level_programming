#!/usr/bin/python3
"""Defines a class Rectangle"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle"""

    def __init__(self, width, height):
        """Intialize a new Rectangle.

        Args:
            width (int): width of the new Rectangle.
            height (int): height of the new Rectangle.
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
