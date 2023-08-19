#!/usr/bin/python3
"""a script that lists cities from the database"""
import MySQLdb
import sys


def main():
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    conn = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=mysql_username,
        passwd=mysql_password,
        db=database_name
    )
    cursor = conn.cursor()

    query = """
    SELECT cities.id, cities.name, states.name
    FROM cities
    JOIN states ON cities.state_id = states.id
    ORDER BY cities.id
    """
    cursor.execute(query)

    city_rows = cursor.fetchall()

    for city_row in city_rows:
        print(city_row)

    cursor.close()
    conn.close()


if __name__ == "__main__":
    main()
