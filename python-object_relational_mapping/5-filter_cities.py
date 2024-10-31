#!/usr/bin/python3
"""
Script that takes in the name of a state as an argument and lists
all cities of that state, using the database hbtn_0e_4_usa
"""

import MySQLdb
import sys


def main():
    """
    Connects to a MySQL database and retrieves all cities of a given state.
    """
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    data_list = []

    try:
        if len(sys.argv) < 5 or len(sys.argv) >= 6:
            raise IndexError("Expected exactly 5 arguments")
        filter = sys.argv[4]

    except IndexError as e:
        print(e)
        sys.exit(1)

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
    cur.execute("SELECT cities.name \
        FROM cities JOIN states \
        ON cities.state_id = states.id \
        WHERE states.name = %s\
        ORDER BY cities.id ASC", (filter,))
    query_rows = cur.fetchall()
    for row in query_rows:
        data_list.append(row[0])
    print(*data_list, sep=", ")

    cur.close()
    conn.close()


if __name__ == "__main__":
    main()
