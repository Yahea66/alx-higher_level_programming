#!/usr/bin/python3
"""Lists states"""

import MySQLdb as db
from sys import argv

if __name__ == "__main__":
    conn = db.connect(
            host="localhost",
            port=3306,
            user=argv[1],
            passwd=argv[2],
            db=argv[3],
            charset="utf8"
            )
    cursor = conn.cursor()
    query = """SELECT * FROM states WHERE name = %s
    ORDER BY states.id"""
    cursor.execute(query, (argv[4],))
    result = cursor.fetchall()
    for row in result:
        print(row)
    cursor.close()
    conn.close()
