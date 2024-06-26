#!/usr/bin/python3
"""Fetches url alx-intranet.hbtn.io status."""


if __name__ == "__main__":
    import requests

    rq = requests.get("https://alx-intranet.hbtn.io/status")
    print("Body response:")
    print("\t- type: {}".format(type(rq.text)))
    print("\t- content: {}".format(rq.text))
