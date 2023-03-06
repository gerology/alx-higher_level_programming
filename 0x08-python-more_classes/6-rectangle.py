#!/usr/bin/python3
""" creates a rectangle """
 
class Rectangle:
    """create an instance of a rectangle"""

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """ new instance of a rectangle"""
        self.width = width
        self.height = height
        type(self).number_of_instances += 1
    @property
    def width(self):
        """retrieve the width"""
        return self.__width
    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value
    @property
    def height(self):
        """ retrieve the height"""
        self.__height = height
    @height.setter
    def height(self, value):
        if  not isinstance(value, int):
            raise ValueError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def __del__(self):
        type(self).number_of_instances -= 1
        print("Bye rectangle...")

    def area(self):
        """return the area of a rectangle"""
        self.area = self.__width * self.__height
        return self.area
    def perimeter(self):
        """ return the perimeter of a rectangle"""
        if self.__width == 0 or self.__height == 0:
            return (0)
        self.perimeter = (self.__width * 2) + (self.__height *2)
        return self. perimeter

    def __str__(self):
        rep = []
        for h in range(self.__height):
            [rep.append("#") for w in range(self.__width)]
            if h != self.__height:
                rep.append("\n")
        return ("".join(rep))

    def __repr__(self):
        """ return the string representation of rectangle"""
        rap = "Rectangle(" + str(self.__width)
        rap += ", " + str(self.__height) + ")"
        return (rap)
    
