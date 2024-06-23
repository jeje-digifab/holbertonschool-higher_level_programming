#!/usr/bin/python3
"""
Script that connects to a MySQL database using MySQLdb and lists all states
from the 'states' table sorted by 'id' in ascending order.
"""

import MySQLdb


def main():
    """ Connect to MySQL database """
    conn = MySQLdb.connect(host="localhost", port=3306, user="root",
                           passwd="root", db="hbtn_0e_0_usa", charset="utf8")

    """ Create a cursor object to execute SQL queries """
    cur = conn.cursor()

    """
    Execute SQL query to select all states
    sorted by 'id' in ascending order
    """
    cur.execute("SELECT * FROM states ORDER BY id ASC")

    """ Fetch all rows from the query result """
    query_rows = cur.fetchall()

    """ Print each row retrieved """
    for row in query_rows:
        print(row)

    """ Close the cursor and the database connection """
    cur.close()
    conn.close()


if __name__ == "__main__":
    main()
