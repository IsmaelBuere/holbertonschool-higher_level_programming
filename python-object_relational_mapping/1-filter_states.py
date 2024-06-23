#!/usr/bin/python3
"""
that lists all states with a name starting with N
"""
import sys
import MySQLdb


def main():
    """
    Connects to the MySQL server and lists all states starting with 'N'.
    """
    if len(sys.argv) != 4:
        print("Usage: ./1-filter_states.py <mysql username> <mysql password> "
              "<database name>")
        return

    username = sys.argv[1]
    password = sys.argv[2]
    dbname = sys.argv[3]

    db = MySQLdb.connect(
        host="localhost", user=username, passwd=password, db=dbname,
        port=3306
    )

    cursor = db.cursor()

    query = "SELECT id, name FROM states WHERE name LIKE 'N%' ORDER BY id ASC"
    cursor.execute(query)

    states = cursor.fetchall()

    for state in states:
        print(state)
    cursor.close()
    db.close()


if __name__ == "__main__":
    main()
