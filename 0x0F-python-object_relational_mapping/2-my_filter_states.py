#!/usr/bin/python3
"""
This module is used to list all states from a specific MySQL database.
It uses MySQLdb to connect to the database and perform
an SQL query to retrieve all states.
"""

import MySQLdb
import sys


def main():
    """
    Main function that uses command line arguments
    to connect to a database and print all states in that database,
    sorted by their IDs.
    """
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    state_name_searched = sys.argv[4]

    db = MySQLdb.connect(
        host="localhost",
        user=mysql_username,
        passwd=mysql_password,
        db=database_name,
        port=3306
    )

    cursor = db.cursor()
    query = "SELECT * FROM states WHERE name LIKE %s ORDER BY id ASC"
    cursor.execute(query, (state_name_searched,))
    results = cursor.fetchall()
    for row in results:
        print(row)

    cursor.close()
    db.close()


if __name__ == "__main__":
    main()
