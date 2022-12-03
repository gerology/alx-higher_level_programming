#!/usr/bin/python3
def uppercase(str):
    """ This function prints strings in uppercase followed by new line"""
    for x in str:
        num = ord(x)
        if num >= 97 and num <= 122:
            num = num - 32
        print("{}".format(chr(num)), end="")
    print()
