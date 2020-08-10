#!/usr/bin/python3
""" adds the State object “Louisiana” to the database hbtn_0e_6_usa
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """ Add a new state
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

    n_state = State(name="Louisiana")
    session.add(n_state)
    session.commit()
    print(n_state.id)

    session.close()
