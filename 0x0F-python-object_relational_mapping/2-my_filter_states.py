#!/usr/bin/python3
"""script that takes in an argument and displays
    all values in the states table of hbtn_0e_0_usa
    where name matches the argument."""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    database = MySQLdb.connect(host='localhost', port=3306, user=argv[1],
                                    passwd=argv[2], db=argv[3])

    sql = """SELECT * FROM states WHERE name \
                LIKE BINARY '%s' ORDER BY id;""" % (argv[4])
    mycursor = database.cursor()
    mycursor.execute(sql)
    result = mycursor.fetchall()
    for value in result:
        print(value)
