#!/usr/bin/python3
"""takes in a URL,
sends a request to the URL and displays the value of the X-Request-Id"""
import sys
import urllib.request


if __name__ == "__main__":
    url = sys.argv[1]
    with urllib.request.urlopen(url) as response:
        headers = response.info()
        print(headers.get("X-Request-Id"))
