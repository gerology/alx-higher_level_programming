#!/usr/bin/python3
def uppercase(str):
    """ This function prints strings in uppercase followed by new line"""
    for x in str:
        num = ord(x)
        if num >= 97 and num <= 122:
            print("{}".format(chr(num - 32)), end="")
        else:
            print("{}".format(chr(num)), end="")
    print()
