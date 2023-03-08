#!/usr/bin/python3
""" define a python to json function"""


def class_to_json(obj):
    """ return the dictionarry representation of simple data structure"""
    return obj.__dict__
