#!/usr/bin/python3

"""
    python module that defines a rectangle class
"""


class Rectangle:

    '''
    This class defines rectangle
    '''

    def __init__(self, width=0, height=0):
        """ initializes new rectangle
        width (int) : width of rectangle

        height (int): height of rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ retieve the width of the rectangle """
        if width < 0:
            raise ValueError("width must be >=0")
        return self.__width

    @width.setter
    def width(self, value):
        """ set width value for the rectangle"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >=0")

        self.__width = value

    @property
    def height(self):
        """ retrieve the height of the rectangle"""
        if height < 0:
           raise ValueError("height must be >=0")
        return self.__height

    @height.setter
    def height(self, value):
        """ retrieve the value of height of the rectangle"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value
