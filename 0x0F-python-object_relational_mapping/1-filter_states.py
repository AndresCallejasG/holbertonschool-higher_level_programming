#!/usr/bin/python3
""" lists all states with a name starting with N (upper N)
    from the database hbtn_0e_0_usa
"""


import sys
import MySQLdb


if __name__ == "__main__":
    """ Filter states
    """
    my_host = 'localhost'
    my_port = 3306
    my_user = sys.argv[1]
    my_passwd = sys.argv[2]
    my_database = sys.argv[3]

    db = MySQLdb.connect(host=my_host, port=my_port,
                         user=my_user, passwd=my_passwd, db=my_database)

    cur = db.cursor()

    cur.execute('SELECT * FROM states')

    rows = cur.fetchall()

    for state in rows:
        if state[1].startswith("N"):
            print(state)

    cur.close()
    db.close()
