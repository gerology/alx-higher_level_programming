#!/usr/bin/python3

"""funtion that deletes a key in the dictionary"""


def simple_delete(a_dictionary, key=""):
    if key in a_dictionary:
        del a_dictionary[key]
    return (a_dictionary)
