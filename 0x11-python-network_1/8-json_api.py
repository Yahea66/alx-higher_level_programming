#!/usr/bin/python3
"""takes in a URL, sends a request to the URL and
displays the body of the response."""
import sys
import requests


if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    arg = ""
    if len(sys.argv) > 1:
        arg = sys.argv[1]
    data = {'q': arg}
    response = requests.post(url, data)
    try:
        r = response.json()
        if r == {}:
            print("No result")
        else:
            print("[{}] {}".format(r.get("id"), r.get("name")))
    except ValueError:
        print("Not a valid JSON")
