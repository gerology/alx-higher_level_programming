#!/usr/bin/python3
""" take a letter and send post request
    to http://0.0.0.0:5000/search_user
    using the letter as parameter

    Usage: ./8-json_api.py <letter>
  - The letter is sent as the value of the variable `q`.
  - If no letter is provided, sends `q=""`
"""

import requests
import sys


if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"

    if len(sys.argv) == 1:
        letter = {"q": ""}
    else:
        letter = {"q": sys.argv[1]}

    sett = requests.post(url, data=letter)
    try:
        check_json = sett.json()
        if check_json == {}:
            print("No result")
        else:
            print("[{}] {}".format(check_json.get("id"), check_json.get("name")))
    except ValueError:
        print("Not a valid JSON")
