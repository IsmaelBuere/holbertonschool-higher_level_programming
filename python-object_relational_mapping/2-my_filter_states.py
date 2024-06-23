#!/usr/bin/python3
"""
that takes in an argument and displays all values in the states
"""
import sys
import MySQLdb


def main():
    """
    Connects to the MySQL server and lists states matching the argument.
    """
    if len(sys.argv) != 5:
        print("Usage: ./2-my_filter_states.py <mysql username> <mysql password>"
              " <database name> <state name searched>")
        return

    username = sys.argv[1]
    password = sys.argv[2]
    dbname = sys.argv[3]
    state_name = sys.argv[4]

    db = MySQLdb.connect(
        host="localhost", user=username, passwd=password, db=dbname,
        port=3306
    )

    cursor = db.cursor()

    query = ("SELECT id, name FROM states WHERE name = '{}' ORDER BY id ASC"
             .format(state_name))
    cursor.execute(query)

    states = cursor.fetchall()

    for state in states:
        print(state)

    cursor.close()
    db.close()


if __name__ == "__main__":
    main()
