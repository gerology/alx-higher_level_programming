#!/usr/bin/python3
""" send request and display the value of the 
    variable X-Request-Id in the response body 
"""

import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]

    sett = requests.get(url)
    val = sett.headers.get("X-Request-Id")
    print(val)
