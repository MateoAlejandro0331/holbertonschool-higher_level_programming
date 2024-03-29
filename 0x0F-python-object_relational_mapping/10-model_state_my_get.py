#!/usr/bin/python3
"""script that prints the State object
    with the name passed as argument from
    the database hbtn_0e_6_usa
"""

import sys
from model_state import Base, State
from sqlalchemy.orm import Session
from sqlalchemy import (create_engine)

if __name__ == "__main__":
    database = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    sesion = Session(database)
    """Query to the database"""
    query = sesion.query(State).order_by(State.id)
    for instance in query:
        if sys.argv[4] == instance.name:
            print(f"{instance.id}")
            exit(0)
    print("Not found")
