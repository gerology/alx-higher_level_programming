#!/usr/bin/python3

""" determine the object is an instance
     of a class or a class inherited from specified class
"""
def is_kind_of_class(obj, a_class):
    """
        returns True if the ibject is an instance 
        of the specified class

        Args:
           obj - object to check
           a_class - class to check objwct against

        rsturn:
           return True if object is an instance of 
           specified class
           else returns False
    """
    if isinstance(obj, a_class):
        return True
    return False

