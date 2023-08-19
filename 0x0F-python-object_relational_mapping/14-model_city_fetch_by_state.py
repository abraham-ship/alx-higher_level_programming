#!/usr/bin/python3
"""a script that prints all city objects in the database"""
from model_state import Base, State
from model_city import City
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)
import sys


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))

    Session = sessionmaker(bind=engine)
    session = Session()

    query = session.query(City, State).\
        filter(City.state_id == State.id).all()
    for city, state in query:
        print('{}: ({}) {}'.format(state.name, city.id, city.name))

    session.close()
