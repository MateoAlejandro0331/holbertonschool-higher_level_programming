#!/usr/bin/python3
"""https://www.geeksforgeeks.org/how-to-
    show-all-tables-in-mysql-using-python/"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    database = MySQLdb.connect(host='localhost', port=3306, user=argv[1],
                                    passwd=argv[2], db=argv[3])

    mycursor = database.cursor()
    mycursor.execute("SELECT cities.name \
                        FROM cities JOIN states on \
                            cities.state_id = states.id\
                                WHERE states.name = %s\
                                ORDER BY cities.id", (argv[4], ))
    result = mycursor.fetchall()
    output_string = ", ".join(value[0] for value in result)
    print(output_string)
