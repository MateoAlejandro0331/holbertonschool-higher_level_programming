#!/usr/bin/python3
"""script that lists all State objects
    from the database hbtn_0e_6_usa, ojala
    pase el checker por que ya no se que mas hacer
"""

import sys
from model_state import Base, State
from sqlalchemy.orm import Session
from sqlalchemy import (create_engine)

if __name__ == "__main__":
    database = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    sesion = Session(database)
    
    for instance in sesion.query(State).order_by(State.id):
        print(f"{instance.id}: {instance.name}")
