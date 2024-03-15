#!/usr/bin/python3
"""
Lists all cities from a specified state in the
`hbtn_0e_4_usa` database, ordered by id.
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':

    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2],
                         db=sys.argv[3], port=3306)

    cursor = db.cursor()
    cursor.execute("""SELECT cities.name
          FROM states
          INNER JOIN cities ON states.id = cities.state_id
          WHERE states.name = %s
          ORDER BY cities.id ASC""", (state_name,))

    print(", ".join([row[0] for row in cursor.fetchall()]))