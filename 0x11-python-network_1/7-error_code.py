
#!/usr/bin/python3
""" display the body of response for request sent to URL"""

import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]

    sett = request.get(url)
    if sett.status_code >= 400:
        print("Error code: {}".format(sett.raise_for_status))
    else:
        print(sett.text)
