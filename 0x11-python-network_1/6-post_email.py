#!/usr/bin/python3
""" that takes in a URL and an email address, sends a POST
"""
import sys
import requests

if __name__ == "__main__":
    urll = sys.argv[1]
    mail = sys[2]
    request = request.post(urll, data={'email': email})
    with urllib.request.urlopen(request) as res:
        print(res.text))
