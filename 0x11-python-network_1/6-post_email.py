#!/usr/bin/python3
""" display body of response for POST request sent to url with email as a parameter"""

import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    dat = {"email": sys.argv[2]}

    sett = requests.post(url, data=dat)
    print("Your email is: {}".format(sett.text))
