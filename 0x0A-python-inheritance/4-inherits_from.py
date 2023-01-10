#!/usr/bin/python3

""" determine if the object is an instance
    a class that inherits directly or indirectly
    from specified class
"""


def inherits_from(obj, a_class):
    """ return true if object is an instance
        of a class the inherits from specified class

        Args:
            obj - object to check
            a_class - class to check against
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
