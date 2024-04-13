#!/usr/bin/python3
"""  lists states from database hbtn_0e_0_usa """
import MySQLdb
import sys


if __name__ == "__main__":
    data = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], data=sys.argv[3], port=3306)
    crs = data.cursor()
    crs.execute("SELECT * FROM states")
    rows = crs.fetchall()
    for row in rows:
        print(row)
    crs.close()
    data.close()
