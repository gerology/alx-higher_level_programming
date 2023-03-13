#!/usr/bin/python3
""" define a class square """


class Square:
    """ defines a new square """
    def __init__(self, size=0, position=(0, 0)):
        """ create a new instance """
        self.__size = size
        self.__position = position
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

    @property
    def position(self):
        """ retrieve position """
        return (self.__position)

    @position.setter
    def position(self, value):
        """ set the value for position """
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """ return the area of the square"""
        return (self.__size * self.__size)
    def my_print(self):
        """ print to stdout with '#' """
        if self.__size == 0:
            print("")
            return

        [print("") for i in range(0, self.__position[1])]
        for c in range(0, self.__size):
            [print(" ", end="") for p in range(0, self.__position[0])]
            [print("#", end="") for m in range(0, self.__size)]
            print("")
