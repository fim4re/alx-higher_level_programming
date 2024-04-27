#!/usr/bin/python3
"""takes in a URL and an email address, sends a POST request
"""
import sys
import requests

if __name__ == '__main__':
    urll = sys.argv[1]
    req = request.get(urll)
    if res.status_code >= 400:
        print("error code: {}".format(res.status_code))
    else:
        print(rq.text)
