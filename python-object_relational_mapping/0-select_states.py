#!/usr/bin/python3
"""
Lists all states from the database hbtn_0e_0_usa
in ascending order by states.id.
"""

import MySQLdb
import sys


def main():
    """Connects to MySQL and lists all states sorted by id."""
    user, pwd, dbname = sys.argv[1], sys.argv[2], sys.argv[3]

    # Connect to MySQL server
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=user,
        passwd=pwd,
        db=dbname,
        charset="utf8"
    )

    cursor = db.cursor()
    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    for row in cursor.fetchall():
        print(row)

    cursor.close()
    db.close()


if __name__ == "__main__":
    main()
