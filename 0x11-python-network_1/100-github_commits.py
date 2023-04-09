#!/usr/bin/python3
"""  """

import requests
import sys


if __name__ == "__main__":
    url = "https://developer.github.com/repos/{}/{}/commits".format(sys.argv[2], sys.argv[1])
    sett = requests.get(url)
    comit = sett.json()
    try:
        for k in range(10):
            print("{}: {}".format(comit[i].get("sha"), comit[i].get("commit").get("author").get("name")))
    except IndexError:
        pass
