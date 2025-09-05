#!/usr/bin/python3
"""Lists all states from the database hbtn_0e_0_usa, sorted by id ascending.

Usage:
    ./0-select_states.py <mysql_user> <mysql_password> <db_name>
"""

import sys
import MySQLdb


def main():
    """Connect to MySQL and print (id, name) for all states ordered by id ASC."""
    user, pwd, dbname = sys.argv[1], sys.argv[2], sys.argv[3]

    db = None
    cursor = None
    try:
        db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=user,
            passwd=pwd,
            db=dbname,
            charset="utf8"
        )
        cursor = db.cursor()
        cursor.execute("SELECT id, name FROM states ORDER BY id ASC;")
        for row in cursor.fetchall():
            print(row)
    except MySQLdb.Error as e:
        print(f"Error connecting to database: {e}")
    finally:
        if cursor is not None:
            cursor.close()
        if db is not None:
            db.close()


if __name__ == "__main__":
    main()

