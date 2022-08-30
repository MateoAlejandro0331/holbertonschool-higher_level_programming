#!/usr/bin/python3
"""ists all states with a name starting with N (upper N)
  https://www.geeksforgeeks.org/sql-query-to-find-the-name-of-
  a-person-whose-name-starts-with-specific-letter/"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    database = MySQLdb.connect(host='localhost', port=3306, user=argv[1],
                                    passwd=argv[2], db=argv[3])

    mycursor = database.cursor()
    mycursor.execute("SELECT * FROM states WHERE name LIKE 'N%';")
    result = mycursor.fetchall()
    for value in result:
        print(value)
