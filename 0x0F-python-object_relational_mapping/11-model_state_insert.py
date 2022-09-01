#!/usr/bin/python3
"""script that adds the State object
    “Louisiana” to the database hbtn_0e_6_usa
    espero pase el checker
"""

import sys
from model_state import Base, State
from sqlalchemy.orm import Session
from sqlalchemy import (create_engine)

if __name__ == "__main__":
    database = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    sesion = Session(database)
    """Create a object an insert to the database"""
    Louisiana = State(name='Louisiana')
    sesion.add(Louisiana)
    sesion.commit()
    """Query to the database"""
    query = sesion.query(State).filter(State.name == 'Louisiana')
    for instance in query:
        print(f"{instance.id}")


