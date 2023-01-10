#!/usr/bin/python3

""" define a model that inherits from a list"""


class MyList(list):
    """ sorted printing """
    def print_sorted(self):
        """ print the list in ascending order"""
        print(sorted(self))
