#!/usr/bin/python3
"""
that lists all states with a name starting with N
"""
import sys
import MySQLdb


import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )

    cur = db.cursor()

    query = ("SELECT * FROM states WHERE name LIKE BINARY 'N%' "
             "ORDER BY states.id ASC")

    cur.execute(query)

    for row in cur.fetchall():
        print(row)

    cur.close()
    db.close()


if __name__ == "__main__":
    main()
