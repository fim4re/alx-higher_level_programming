#!/usr/bin/python3
"""takes in a URL and an email address, sends a POST request
"""
import sys
import requests

if __name__ == '__main__':
    urll = sys.argv[1]
    email = sys.argv[2]
    rq = requests.post(urll, data={'email': email})
    print(rq.text)
