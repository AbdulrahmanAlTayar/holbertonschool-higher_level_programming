#!/usr/bin/python3
"""
Displays all values in states where name matches the argument (unsafe).
"""

import sys
import MySQLdb


def main():
    """Connects and fetches states where name matches the given argument."""
    username, password, database, state_name = (
        sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]
    )
    db = MySQLdb.connect(host="localhost", port=3306, user=username,
                         passwd=password, db=database, charset="utf8")
    cur = db.cursor()
    query = ("SELECT * FROM states WHERE BINARY name = '{}' "
             "ORDER BY id ASC;").format(state_name)
    cur.execute(query)
    for row in cur.fetchall():
        print(row)
    cur.close()
    db.close()


if __name__ == "__main__":
    main()
