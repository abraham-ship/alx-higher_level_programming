#!/usr/bin/python3
"""a script that deletes all state objects containing letter `a`
from the database"""
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)
import sys


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))

    Session = sessionmaker(bind=engine)

    session = Session()
    states = session.query(State).filter(State.name.contains('a'))

    for state in states:
        session.delete(state)
    session.commit()
    session.close
