#!/usr/bin/python3
def uppercase(str):
    """ This function prints strings in uppercase followed by new line"""
    for x in str:
        if ord(x) >= 97 and ord(x) <= 122:
            x = chr(ord(x) - 32)
        print(f"{x}")
    print()
