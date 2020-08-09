#!/usr/bin/python3
""" takes in an argument and displays all values in the states table
    of hbtn_0e_0_usa where name matches the argument.
    safe from MySQL injections!
"""


import sys
import MySQLdb


if __name__ == "__main__":
    """ SQL Injection...
    """
    my_host = 'localhost'
    my_port = 3306
    my_user = sys.argv[1]
    my_passwd = sys.argv[2]
    my_database = sys.argv[3]
    name = sys.argv[4]

    db = MySQLdb.connect(host=my_host, port=my_port,
                         user=my_user, passwd=my_passwd, db=my_database)
    cur = db.cursor()

    cur.execute("SELECT * FROM states WHERE name =%(name)s",
                {
                    'name': name
                })
    rows = cur.fetchall()

    for state in rows:
            print(state)

    cur.close()
    db.close()
