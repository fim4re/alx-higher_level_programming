#!/usr/bin/python3
""" mdl lists all states from the hbtn_0e_0_usa """
import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    crs = db.cursor()
    crs.execute("SELECT * FROM states WHERE name LIKE BINARY '{}'"
                .format(sys.argv[4]))
    rows = crs.fetchall()
    for row in rows:
        print(row)
