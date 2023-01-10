#!/usr/bin/python3

""" defines a class that validates value
    and raises exception with wrong values
"""


class BaseGeometry:
    """ defines a class 'BaseGeometry' """

    def area(self):
        """raise exception """
        raise Exception("area() is not implemented")

    def __init__(self):
        pass

    def integer_validator(self, name, value):
        """ validate value """
        self.name = name

        if not type(value) == int:
            raise TypeError("{} must be an integer".format(self.name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(self.name))
        self.value = value
