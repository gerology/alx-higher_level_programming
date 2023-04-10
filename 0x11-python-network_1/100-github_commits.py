#!/usr/bin/python3
""" print commits """

import requests
import sys


if __name__ == "__main__":
    url = "https://api.github.com/repos/{}/{}/commits".format(
            sys.argv[2],
            sys.argv[1])
    sett = requests.get(url)
    comit = sett.json()
    try:
        for k in range(10):
            print("{}: {}".format(
                comit[k].get("sha"),
                comit[k].get("commit").get("author").get("name")))
    except IndexError:
        pass
