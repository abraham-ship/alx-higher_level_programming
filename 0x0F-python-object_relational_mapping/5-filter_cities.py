#!/usr/bin/python3
"""a script that lists cities of a state from the database"""
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

    query = """
    SELECT cities.name FROM cities
    JOIN states ON cities.state_id = states.id WHERE states.name = %s
    ORDER BY cities.id
    """
    cursor.execute(query, (user_state,))

    city_rows = cursor.fetchall()

    print(", ".join([row[0] for row in city_rows]))

    cursor.close()
    conn.close()


if __name__ == "__main__":
    main()
