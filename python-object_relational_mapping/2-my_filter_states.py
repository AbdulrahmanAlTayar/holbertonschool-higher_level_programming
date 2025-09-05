#!/usr/bin/python3
"""
Lists all states where name matches the argument (unsafe format).
"""

import sys
import MySQLdb


def main():
    """Connect to MySQL and fetch states matching the given name."""
    user, pwd, dbname, state_name = (
        sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]
    )

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=user,
        passwd=pwd,
        db=dbname,
        charset="utf8"
    )

    cursor = db.cursor()
    # Intentionally unsafe per task: build query with format()
    query = (
        "SELECT id, name FROM states "
        "WHERE name = '{}' "
        "ORDER BY id ASC;"
    ).format(state_name)

    cursor.execute(query)
    for row in cursor.fetchall():
        print(row)

    cursor.close()
    db.close()


if __name__ == "__main__":
    main()
