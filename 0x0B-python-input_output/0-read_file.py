#!/usr/bin/python3


def read_file(filename=""):
    """ read text file and output to stdout"""
    with open(filename, encoding="utf-8") as f:
        read = f.read()
    print(read)
