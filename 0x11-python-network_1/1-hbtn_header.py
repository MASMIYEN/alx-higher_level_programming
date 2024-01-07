#!/usr/bin/python3
"""Displays the value of the X-Request-Id
variable found in the header"""
import urllib.request
import sys

if __name__ == "__main__":
    url = sys.argv[1]

    request = urllib.request.Request(url)
    with urllib.request.urlopen(request) as response:
        print(response.headers.get("X-Request-Id"))