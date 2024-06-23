#!/usr/bin/python3
"""
Script that connects to a MySQL database using MySQLdb and lists all cities
from the database 'hbtn_0e_4_usa'. The script takes 3 arguments: mysql
username, mysql password, and database name. Results are sorted by 'cities.id'
in ascending order.
"""

import sys
import MySQLdb


def main():
    """
    Main function to connect to the MySQL database and list all cities
    sorted by 'cities.id' in ascending order.
    """
    if len(sys.argv) != 4:
        print("Usage: {} <mysql username> <mysql password> <database name>"
              .format(sys.argv[0]))
        return

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
    query = ("SELECT cities.id, cities.name, states.name "
             "FROM cities JOIN states ON cities.state_id = states.id "
             "ORDER BY cities.id ASC")
    cur.execute(query)
    query_rows = cur.fetchall()
    for row in query_rows:
        print("{:}".format(row))
    cur.close()
    conn.close()


if __name__ == "__main__":
    main()
