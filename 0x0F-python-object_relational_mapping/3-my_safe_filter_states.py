#!/usr/bin/python3
""" displays all values in the states from the database hbtn_0e_0_usa """
import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    crs = db.cursor()
    # sql query
    m = sys.argv[4]
    crs.execute("SELECT * FROM states WHERE name LIKE %s", (m, ))
    # fetch all rows
    rows = crs.fetchall()
    for row in rows:
        print(row)
