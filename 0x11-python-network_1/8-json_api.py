#!/usr/bin/python3
""" take a letter and send post request to http://0.0.0.0:5000/search_user using the letter as parameter """

import requests
import sys


if __name__ == "__main__":
    letter = {"q": sys.argv[1]}
    url = "http://0.0.0.0:5000/search_user"
    
    if len(sys.argv) == 1:
        sett = requests.post(url, data="")
    else:
        sett = requests.post(url, q=letter)

    try:
        check_json = sett.json()
        if check_json == {}:
            print("No result")
    else:
        print("[{}] {}".format(check_json.get("id"), check_json.get("name")))
