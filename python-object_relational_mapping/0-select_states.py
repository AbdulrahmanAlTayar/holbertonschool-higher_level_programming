#!/usr/bin/python3
"""Lists all states from the database hbtn_0e_0_usa.

Usage:
    ./0-select_states.py <mysql_user> <mysql_password> <db_name>

Constraints:
    - Uses MySQLdb (mysqlclient).
    - Connects to localhost:3306.
    - Results sorted by states.id ASC.
"""

import sys
import MySQLdb


def main():
    """Entry point."""
    user, pwd, dbname = sys.argv[1], sys.argv[2], sys.argv[3]
    conn = MySQLdb.connect(
        host="localhost", port=3306, user=user, passwd=pwd, db=dbname, charset="utf8"
    )
    cur = conn.cursor()
    cur.execute("SELECT id, name FROM states ORDER BY id ASC;")
    for row in cur.fetchall():
        print(row)
    cur.close()
    conn.close()


if __name__ == "__main__":
    main()

