#!/usr/bin/python3

""" defines a square class that inheritsfrom rectangle"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ 
     creates a square class that
     inherits from Rectangle class
    """
    def __init__(self, size):
        """Initialize a new square.
        Args:
            size (int): The size of the new square.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
