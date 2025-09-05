#!/usr/bin/python3
"""
Safely displays all values in states where name matches the argument.
"""

import sys
import MySQLdb


def main():
    """Connects and safely fetches states matching the given name."""
    username, password, database, state_name = (
        sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]
    )
    db = MySQLdb.connect(host="localhost", port=3306, user=username,
                         passwd=password, db=database, charset="utf8")
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE BINARY name = %s "
                "ORDER BY id ASC;", (state_name,))
    for row in cur.fetchall():
        print(row)
    cur.close()
    db.close()


if __name__ == "__main__":
    main()
