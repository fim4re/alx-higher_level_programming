#!/usr/bin/python3
"""takes in a URL and an email address, sends a POST request
"""


if __name__ == '__main__':
    import sys
    import requests

    urll = sys.argv[1]
    mail = sys.argv[2]
    rq = requests.post(urll, data={'email': mail})
    print(rq.text)
