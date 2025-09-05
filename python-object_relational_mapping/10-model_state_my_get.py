#!/usr/bin/python3
"""
Prints the State object with the name passed as argument.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import Base, State

if __name__ == "__main__":
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        ),
        pool_pre_ping=True
    )
    session = Session(engine)
    name = sys.argv[4]
    state = session.query(State).filter(State.name == name).first()
    if state:
        print(state.id)
    else:
        print("Not found")
    session.close()
