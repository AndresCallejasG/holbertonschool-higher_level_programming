#!/usr/bin/python3
""" prints the State object with the name
    passed as argument from the database hbtn_0e_6_usa
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """ Get a state
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

    state = session.query(State).filter(State.name == sys.argv[4]).first()
    if state:
        print(state.id)
    else:
        print('Not found')

    session.close()
