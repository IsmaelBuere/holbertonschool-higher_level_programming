#!/usr/bin/python3
"""
script that takes in an argument and displays all values in the states
"""
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
    state = sys.argv[4]

    query = ("SELECT * FROM states WHERE BINARY name = '{}' "
             "ORDER BY states.id ASC").format(state)

    cur.execute(query)

    for row in cur.fetchall():
        print(row)

    cur.close()
    db.close()
