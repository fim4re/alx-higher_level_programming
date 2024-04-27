#!/usr/bin/python3
""" that takes in a URL and an email address, sends a POST
"""
import sys
import requests

if __name__ == "__main__":
    urll = sys.argv[1]

    request = urllib.request.Request(urll)
    with urllib.request.urlopen(request) as res:
        print(dict(res.headers).get("X-Request-Id"))
