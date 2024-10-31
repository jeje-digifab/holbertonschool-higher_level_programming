#!/usr/bin/python3
"""
Script that lists all cities from the database hbtn_0e_4_usa
"""

import MySQLdb
import sys


def main():
    """
    Connects to a MySQL database and retrieves all cities along
    with their corresponding state names.
    """
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=mysql_username,
        passwd=mysql_password,
        db=database_name,
        charset="utf8"
    )
    cur = conn.cursor()
    # HERE I have to know SQL to grab all states in my database
    cur.execute("SELECT cities.id, cities.name, states.name \
        FROM cities JOIN states \
        ON cities.state_id = states.id ORDER BY cities.id ASC")
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()


if __name__ == "__main__":
    main()
