#!/usr/bin/python3
""" send a request and display the body of response decoded in utf-8 """

import urllib.error
import urllib.request
import sys


if __name__ == "__main__":
    url = sys.argv[1]

    try:
        sett = urllib.request.Request(url)
        with request.urlopen(sett) as fyl:
            print(fyl.read().decode('ascii'))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
