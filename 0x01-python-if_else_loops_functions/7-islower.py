#!/usr/bin/python3
def islower(c):
    """ a function that checks for lowercase characters"""
    num = ord(c)
    for x in range(97, 123):
        if num == x:
            return True
