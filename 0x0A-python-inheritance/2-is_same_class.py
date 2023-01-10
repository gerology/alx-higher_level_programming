#!/usr/bin/python3

"""  check if object is an exact insatnce of specified class"""


def is_same_class(obj, a_class):
    """ returns True if object is an exact instance
       of class specified; else false

       args:
       obj - object to compare to class
       a_class - class by which objwct is compared

       Return:
          True if the object is an exact instance
          of specified class
          else return false
    """
    if type(obj) == a_class:
        return True
    else:
        return False
