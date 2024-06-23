#!/usr/bin/python3
"""
takes in arguments and displays all values in the states table of hbtn_0e_0_usa
"""
if __name__ == "__main__":
    import MySQLdb
    import sys
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database

    )

    cur = db.cursor()
    arg = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
    cur.execute(arg, (state_name,))
    states = cur.fetchall()

    for row in states:
        print(row)

    cur.close()
    db.close()