#!/usr/bin/python3
"""
Lists all states from the database hbtn_0e_0_usa
"""


import sys
import MySQLdb

if __name__ == '__main__':
    db = MySQLdb.connect(port=3306, host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])

    cursor = db.cursor()
    cursor.execute('SELECT * FROM states ORDER BY id ASC')
    states = cursor.fetchall()
    
    for row in states:
        print(row)
    cursor.close()
    db.close()