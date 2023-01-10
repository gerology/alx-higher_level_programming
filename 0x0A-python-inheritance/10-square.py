#!/usr/bin/python3

""" define a square class that inherits from Rectangle """

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
       Square class created with
       inheritance from Rectangle class
    """

    def __init__(self, size):
        """ initialize new instance """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
