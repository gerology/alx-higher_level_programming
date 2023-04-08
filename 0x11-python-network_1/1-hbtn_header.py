#!/usr/bin/python3
""" display the value of the X-Request-Id """
import urllib.request
import sys


if __name__ == "__main__":
    url = sys.argv[1]

    sett = urllib.request.Request("url")
    with urllib.request.urlopen(sett) as fyl:
        print(dict(fyl.headers).get("X-Request-Id"))
