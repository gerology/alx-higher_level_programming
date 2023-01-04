#!/usr/bin/python3


class Rectangle:

    """
    This class defines rectangle by width
    and height based on 0-rectangle.py
    """

    def __init__(self, width=0, height=0):
        """ initializes the data """

        self.__width = width
        self.__height = height

    def set_width(self, value):
        """ set width value """

        self.__value = value

        if type(self.__width) != int:
            raise TypeError("width must be an integer")

        if self.__width < 0:
            raise ValueError("with must be >=0")

    def get_height(self):
        """ retrieve the height """

        return self.__height

    def set_height(self, value):
        """ retrieve the value of height """

        self.__value = value

        if type(self.__height) == int:
            raise TypeError("height must be an integer")

        if (self.__height) < 0:
            raise ValueError("height must be >= 0")
