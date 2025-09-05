#!/usr/bin/python3
"""
Lists all cities of a given state, SQL injection free.
"""

import sys
import MySQLdb


def main():
    """Prints city names of the given state, comma-separated by cities.id."""
    username, password, database, state_name = (
        sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]
    )
    db = MySQLdb.connect(host="localhost", port=3306, user=username,
                         passwd=password, db=database, charset="utf8")
    cur = db.cursor()
    cur.execute(
        "SELECT cities.name FROM cities "
        "JOIN states ON cities.state_id = states.id "
        "WHERE states.name = %s "
        "ORDER BY cities.id ASC;", (state_name,)
    )
    names = [row[0] for row in cur.fetchall()]
    print(", ".join(names))
    cur.close()
    db.close()


if __name__ == "__main__":
    main()
