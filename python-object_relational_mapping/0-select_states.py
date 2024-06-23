#!/usr/bin/python3
"""
that lists all states from the database
"""


import MySQLdb


def get_states(username, password, database):
    """
    Connects to the MySQL
    """
    try:
        db_connection = MySQLdb.connect(host='localhost', user=username, passwd=password, db=database)
    except MySQLdb.Error as e:
        print(f"Error connecting to the database: {e}")
        return

    cursor = db_connection.cursor()

    query = "SELECT id, name FROM states ORDER BY id"
    cursor.execute(query)

    for row in cursor.fetchall():
        state_id, state_name = row
        print(f"({state_id}, '{state_name}')")

    db_connection.close()

if __name__ == "__main__":
    username = input("Enter MySQL username: ")
    password = input("Enter MySQL password: ")
    database = input("Enter database name: ")

    get_states(username, password, database)