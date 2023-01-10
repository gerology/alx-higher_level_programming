#!/usr/bin/python3

""" define a class that inherits """

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ rectangle inherits BaseGeometry """

    def __init__(self, width, height):
        """ initialize a new instance """
        BaseGeometry.__init__(self)
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """ implementation of area) """
        return (self.__width * self.__height)

    def __str__(self):
        """ print strings """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
