#!/usr/bin/python3

""" model for a Rectangle """


class Rectangle:
    """ defines a rectangle class """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
            initialise a new rectangle
            width (int): width of the rectangle
            height (int): height of the rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ get the width of triangle"""

        return self.__width

    @width.setter
    def width(self, value):
        """set width for rectangle """

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ retrieve the height"""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise ValueError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def __del__(self):
        type(self).number_of_instances -= 1
        print("Bye rectangle...")

    def area(self):
        """return the area of a rectangle"""
        area = self.__width * self.__height
        return (area)

    def perimeter(self):
        """ return the perimeter of a rectangle"""
        if self.__width == 0 or self.__height == 0:
            return (0)
        if self.__width == 0 or self.__height == 0:
            return ("")
        self.perimeter = (self.__width * 2) + (self.__height * 2)
        return self. perimeter

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return (rect_1)
        return(rect_2)

    @classmethod
    def square(cls, size=0):
        return (cls(size, size))

    def __str__(self):
        rep = []
        for h in range(self.__height):
            for w in range(self.__width):
                rep.append(str((self).print_symbol))
            if h != self.__height - 1:
                rep.append("\n")
        return ("".join(rep))

    def __repr__(self):
        """ return the string representation of rectangle"""
        rap = "Rectangle(" + str(self.__width)
        rap += ", " + str(self.__height) + ")"
        return (rap)
