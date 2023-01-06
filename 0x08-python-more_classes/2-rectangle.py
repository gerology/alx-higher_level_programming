#!/usr/bin/python3

"""
    define a class Rectangle'
"""


class Rectangle:

    """a model for a rectangle """

    def __init__(self, width=0, height=0):
        """
            initialise a new rectangle

            width (int): width of the rectangle

            height (int): height of the rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ get the width of triangle"""

        return self.__width

    @width.setter
    def width(self, value):
        """set width for rectangle """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ get the height for rectangle """
        return self.__height

    @height.setter
    def height(self, value):
        """ set height of rectangle"""

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ get the area of rectangle """
        self.__area = self.__height * self.__width
        return self.__area

    def perimeter(self):
        """ get perimeter of rectangle"""
        if self.__width == 0 or self.__height == 0:
            return self.parameter == 0
        else:
            self.parameter = 2 * (self.__height + self.__width)
            return self.parameter
