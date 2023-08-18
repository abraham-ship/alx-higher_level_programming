#!/usr/bin/python3
"""a script that lists all states via alchemysql"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    user = sys.argv[1]
    pwd = sys.argv[2]
    db = sys.argv[3]
    engine = create_engine(f'mysql+mysqldb://{user}:{pwd}@localhost:3306/{db}')

    Session = sessionmaker(bind=engine)
    session = Session()

    query = session.query(State).order_by(State.id).all()

    for row in query:
        print(f"{row.id}: {row.name}")

    session.close()
