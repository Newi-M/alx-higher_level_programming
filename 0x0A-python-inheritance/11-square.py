#!/usr/bin/python3
"""Module that holds the class BaseGeometry"""


class BaseGeometry:
    """BaseGeometry class"""

    def area(self):
        """Calculates the area"""

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates input"""

        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """Inherits from BaseGeometry"""

    def __init__(self, width, height):
        """Initializes the class
            Args:
                width (int): width of rectangle
                height (int): height of rectangle
        """

        self.integer_validator("width", width)
        self.__width = width

        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """Calculates area for a rectangle"""

        return self.__width * self.__height

    def __str__(self):
        """Returns rectangle represention"""

        return ("[Rectangle] {}/{}".format(self.__width, self.__height))


class Square(Rectangle):
    """Class that inherits from Rectangle - makes a square"""

    def __init__(self, size):
        """Initializes a square
            Args:
                size (int): size of the square
        """

        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def __str__(self):
        """Returns square represention"""

        return "[Square] {}/{}".format(self.__size, self.__size)
