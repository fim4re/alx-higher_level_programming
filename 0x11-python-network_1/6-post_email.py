#!/usr/bin/python3
""" that takes in a URL and an email address, sends a POST
"""
import sys
import requests

if __name__ == "__main__":
    urll = sys.argv[1]
    email = sys.argv[2]
    res = requests.post(urll, data={'email': email})
    print(res.text)
