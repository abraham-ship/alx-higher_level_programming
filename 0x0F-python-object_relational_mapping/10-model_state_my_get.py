#!/usr/bin/python3
"""a script that prints state object from argument passed from the database"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys


if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))

    Session = sessionmaker(bind=engine)
    session = Session()

    state_name = sys.argv[4]

    searched_state = session.query(State).filter(State.name ==
                                                 state_name).first()

    if searched_state:
        print(searched_state.id)
    else:
        print("Not found")

    session.close()
