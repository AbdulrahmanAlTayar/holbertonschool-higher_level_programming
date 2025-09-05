#!/usr/bin/python3
"""
Lists all states with a name starting with 'N' (upper N)
from the database hbtn_0e_0_usa.
"""

import MySQLdb
import sys


def main():
    """Connects to MySQL and lists states starting with 'N'."""
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
    cursor.execute(
        "SELECT * FROM states "
        "WHERE name LIKE 'N%' "
        "ORDER BY id ASC"
    )

    for row in cursor.fetchall():
        print(row)

    cursor.close()
    db.close()


if __name__ == "__main__":
    main()
