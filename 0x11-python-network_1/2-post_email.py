#!/usr/bin/python3
""" takes an email and url and send a 
    post requestwith email as parameter
"""

import urllib.request
import urllib.parse
import sys

if __name__ = "__main__":
    url = sys.argv[1]
    val = {"email": sys.argv[2]}
    dat = urllib.parse(val).encode('ascii')
    
    sett = urllib.request.Request(url, dat)
    with urllib.request.url(sett) as fyl:
        print(fyl.read().decode("utf-8"))

