#!/usr/bin/python3
""" take my github credentials and use github API to display my id """

import requests
import sys
from requests.auth import HTTPBasicAuth


if __name__ == "__main__":
    auth = HTTPBasicAuth(sys.argv[1], sys.argv[2])
    url = "https://api.github.com/user"
    sett = requests.get(url, auth=auth)
    print(sett.json().get("id"))
