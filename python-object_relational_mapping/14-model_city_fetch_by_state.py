#!/usr/bin/python3
"""
Prints all City objects with their State name.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import Base, State
from model_city import City

if __name__ == "__main__":
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        ),
        pool_pre_ping=True
    )
    session = Session(engine)
    for city, state in session.query(City, State).join(State).order_by(City.id):
        print(f"{state.name}: ({city.id}) {city.name}")
    session.close()
