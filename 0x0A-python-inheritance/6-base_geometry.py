#!/usr/bin/python3

""" define a class 'BaseGeometry' """


class BaseGeometry:
    """ representation of BaseGeometry"""

    def area(self):
        """ raise exception if not implemented """
        raise Exception("area() is not implemented")
