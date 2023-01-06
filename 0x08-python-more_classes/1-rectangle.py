#!/usr/bin/python3

"""
    python module that defines a rectangle class
"""


class Rectangle:

    '''
    This class defines rectangle
    '''

    def __init__(self, width=0, height=0):
        """ initializes new rectangle """

        self.__width = width
        self.__height = height

    def get_width(self):
        """ retieve the width of the rectangle """
        return self.__width

    def set_width(self, value):
        """ set width value for the rectangle"""

        if not isinstance(value, int):
            raise TypeError("width must be an integer")

        if value < 0:
            raise ValueError("with must be >=0")

        self.__width = value

    def get_height(self):
        """ retrieve the height of the rectangle"""

        return self.__height

    def set_height(self, value):
        """ retrieve the value of height of the rectangle"""

        if not isinstance(value, int):
            raise TypeError("height must be an integer")

        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value

