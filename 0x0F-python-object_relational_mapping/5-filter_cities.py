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
    cur = conn.cursor()
    query = """
    SELECT cities.name
    FROM cities
    JOIN states ON cities.state_id = states.id
    where states.name = %s
    ORDER BY cities.id ASC
    """
    cur.execute(query, (argv[4],))
    rows = cur.fetchall()
    print(", ".join(map(lambda x: x[0], rows)))
    cur.close()
    conn.close()
