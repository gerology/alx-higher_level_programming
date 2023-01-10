#!/usr/bin/python3

""" defines a Rectangle class that
    inherits from BaseGeometry
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ Rectangle calss inherits from BaseGeometry """
    def __init__(self, width, height):
        """ instantiate width and height """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
