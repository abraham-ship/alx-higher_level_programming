#!/usr/bin/python3
"""a script that filters states by user input"""
import MySQLdb
import sys


def main():
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    user_state = sys.argv[4]

    conn = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=mysql_username,
        passwd=mysql_password,
        db=database_name
    )

    cursor = conn.cursor()
    query = """SELECT * FROM states WHERE name = '{}' ORDER BY
    states.id""".format(user_state)
    cursor.execute(query)

    state_rows = cursor.fetchall()

    for state_row in state_rows:
        print(state_row)

    cursor.close()
    conn.close()


if __name__ == "__main__":
    main()
