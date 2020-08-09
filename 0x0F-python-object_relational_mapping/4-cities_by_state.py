#!/usr/bin/python3
""" lists all cities from the database hbtn_0e_4_usa
    safe from MySQL injections!
"""


import sys
import MySQLdb


if __name__ == "__main__":
    """ Cities by states
    """
    my_host = 'localhost'
    my_port = 3306
    my_user = sys.argv[1]
    my_passwd = sys.argv[2]
    my_database = sys.argv[3]

    db = MySQLdb.connect(host=my_host, port=my_port,
                         user=my_user, passwd=my_passwd, db=my_database)
    cur = db.cursor()

    cur.execute("""SELECT cities.id, cities.name, states.name
                   FROM cities, states
                   WHERE cities.state_id = states.id
                   ORDER BY cities.id ASC""")
    rows = cur.fetchall()

    for state in rows:
            print(state)

    cur.close()
    db.close()
