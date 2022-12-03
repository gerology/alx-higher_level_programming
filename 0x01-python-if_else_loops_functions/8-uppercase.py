#!/usr/bin/python3
def uppercase(str):
    """ This function prints strings in uppercase followed by new line"""
    for x in str:
        if num >= 97 and num <= 122:
            num = chr(ord(num) - 32)
        print("{}".format(num), end="")
    print("")
