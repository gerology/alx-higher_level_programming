#!/usr/bin/python3
""" fetches https://alx-intranet.hbtn.io/status """
import requests


if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"
    sett = requests.get(url)
    fyl = sett.read()
    print("Body response:")
    print("\t- type: {}".format(type(fyl.text)))
    print("\t- content: {}".format(fyl.text))
