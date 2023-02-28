#!/usr/bin/python3

def complex_delete(a_dictionary, value):
    if not value:
        return (a_dictionary)
    for k, v in a_dictionary.copy().items():
        if v == value:
            del a_dictionary[k]
