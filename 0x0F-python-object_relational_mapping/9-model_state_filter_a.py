#!/usr/bin/python3
""" lists all State objects that contain the
    letter a from the database hbtn_0e_6_usa
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """ Contains `a`
    """
    my_host = 'localhost'
    my_port = 3306
    my_user = sys.argv[1]
    my_passwd = sys.argv[2]
    my_database = sys.argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@{}:{}/{}'.format(
        my_user, my_passwd, my_host, my_port, my_database))
    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).filter(State.name.contains('a'))\
        .order_by(State.id)
    for instance in states:
        print("{}: {}".format(instance.id, instance.name))

    session.close()
