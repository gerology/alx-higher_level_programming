#!/usr/bin/python3

""" model for a Rectangle """


class Rectangle:
    """ defines a rectangle class """

    def __init__(self, width=0, height=0):
        """
            initialise a new rectangle
            width (int): width of the rectangle
            height (int): height of the rectangle
        """
        self.width = width
        self.height = height







        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value
         
    @property
    def height(self):
        """ get the height for rectangle """
        return self.__height

    @height.setter
    def height(self, value):
        """ set height of rectangle"""

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
    
    def area(self):
        """ get the area of rectangle """
        self.__area = self.__height * self.__width
        return self.__area

    def __str__(self):

        if self.__width == 0 or self.__height == 0:
            return ("")

        asterix = []
        for h in range(self.__height):
            [asterix.append('#') for w in range(self.__width)]
            if h != self.__height - 1:
                asterix.append("\n")
        return ("".join(asterix))

    def perimeter(self):
        """ get perimeter of rectangle"""
        if self.__width == 0 or self.__height == 0:
            return (0)

        else:
            self.perimeter = 2 * (self.__height + self.__width)
            return self.perimeter

    def __repr__(self):
        """ return the string representation of rectangle"""
        asterix = "Rectangle(" + str(self.__width)
        asterix += ", " + str(self.__height) + ")"
        return (asterix)
