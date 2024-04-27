#!/usr/bin/python3
"""Lists the 10 most recent commits on a given repository.
"""
import sys
import requests


if __name__ == "__main__":
    urll = "https://api.github.com/repos/{}/{}/commits".format(
        sys.argv[2], sys.argv[1])

    rq = requests.get(urll)
    comm = rq.json()
    try:
        for i in range(10):
            print("{}: {}".format(
                comm[i].get("sha"),
                comm[i].get("commit").get("author").get("name")))
    except IndexError:
        pass
