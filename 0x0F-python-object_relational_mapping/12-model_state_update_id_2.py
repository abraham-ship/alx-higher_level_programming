#!/usr/bin/python3
"""a script that changes name of a state object from the database"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))

    Session = sessionmaker(bind=engine)
    session = Session()

    new = session.query(State).filter(State.id == 2).one()
    new.name = 'New Mexico'
    session.commit()
    session.close
