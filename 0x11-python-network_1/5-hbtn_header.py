#!/usr/bin/python3
"""
 takes in a URL, sends a request to the URL
"""


if __name__ == '__main__':
    import requests
    import sys

    urll = sys.argv[1]

    rq = requests.get(urll)
    print(rq.headers.get('X-Request-Id'))
