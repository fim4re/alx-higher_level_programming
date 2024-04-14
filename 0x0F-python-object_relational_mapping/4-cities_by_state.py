#!/usr/bin/python3
"""  lists all cities from hbtn_0e_0_usa """
import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    crs = db.cursor()
    crs.execute("""SELECT cities.id, cities.name, states.name FROM
                cities INNER JOIN states ON states.id=cities.state_id""")
    # fetch all rows
    rows = crs.fetchall()
    for row in rows:
        print(row)
