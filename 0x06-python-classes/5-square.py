#!/usr/bin/python3

class Square:

    def __init__(self, size=0):
        """ create a new instance """
        self.__size = size
    @property
    def size(self):
        """ retrieve size"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """ set the value for size"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """ return the area of the square"""
        return (self.__size * self.__size)
    def my_print(self):
        """ print to stdout with '#' """
        if self.__size == 0:
            print("")
        for c in range(self.__size):
            print(self.__size * '#')
