#!/usr/bin/python3
""" takes in the name of a state as an argument and lists all
    cities of that state, using the database hbtn_0e_4_usa
    safe from MySQL injections!
"""


import sys
import MySQLdb


if __name__ == "__main__":
    """ All cities by state
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

    cur.execute("""SELECT cities.name
                   FROM cities
                   WHERE cities.state_id = (SELECT id FROM states
                   WHERE name =%(name)s)
                   ORDER BY cities.id""", {'name': name})
    rows = cur.fetchall()
    cities = []
    for city in rows:
        cities.append(city[0])
    print(", ".join(cities))

    cur.close()
    db.close()
