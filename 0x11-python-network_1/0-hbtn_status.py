#!/usr/bin/python3
""" fetch url """


if __name__ == '__main__':
    import urllib.request

    req = urllib.request.Request("https://alx-intranet.hbtn.io/status")
    with urllib.request.urlopen(req)as response:
        con = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(con)))
        print("\t- content: {}".format(con))
        print("\t- utf8 content: {}".format(con.decode('utf-8')))
