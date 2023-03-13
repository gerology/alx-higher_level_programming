#!/usr/bin/python3
""" define a class square """


class Square:
    """ defines a new square """
    def __init__(self, size=0):
        """ new instance of a square"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """ returns the area of a square"""
        return (self.__size * self.__size)
