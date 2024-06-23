#!/usr/bin/python3
"""
Script that connects to a MySQL database using MySQLdb and lists all values in
the 'states' table where name matches the argument. The script takes
4 arguments: mysql username, mysql password, database name, and state name
searched. Results are sorted by 'id' in ascending order.
"""

import MySQLdb
import sys


def main():
    """ Get the arguments from the command line """
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    """ Connect to MySQL database """
    conn = MySQLdb.connect(host="localhost", port=3306, user=username,
                           passwd=password, db=database, charset="utf8")

    """ Create a cursor object to execute SQL queries """
    cur = conn.cursor()

    """
    Execute SQL query to select all states where name matches
    the argument, sorted by 'id' in ascending order
    """
    query = "SELECT * FROM states WHERE name = '{}' ORDER BY id ASC".format(
        state_name)
    cur.execute(query)

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
