#!/usr/bin/python3
""" fetch https://alx-intranet.hbtn.io/status """
import urllib.request


if __name__ == "__main__":
    respond = urllib.request.Request("https://alx-intranet.hbtn.io/status")
    with urllib.request.urlopen(respond) as fyl:
        resp = fyl.read()
        print("Body response:")
        print("\t - type: {}".format(type(resp)))
        print("\t - content: {}".format(resp))
        print("\t - utf8 content: {}".format(resp.decode("utf-8")))
