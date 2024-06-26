#!/usr/bin/python3

""" lists all states from the hbtn_0e_0_usa."""

import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    crs = db.cursor()

    q = ("SELECT * FROM `cities` as `c` \
                INNER JOIN `states` as `s` \
                   ON `c`.`state_id` = `s`.`id` \
                ORDER BY `c`.`id`")
    crs.execute(q)

    print(", ".join([c[2] for c in crs.fetchall() if c[4] == sys.argv[4]]))
    crs.close()
    db.close()
