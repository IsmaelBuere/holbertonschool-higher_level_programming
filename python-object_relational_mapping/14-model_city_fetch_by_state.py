#!/usr/bin/python3
"""
This script prints all City objects from the database hbtn_0e_14_usa.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City

if __name__ == "__main__":
    usr = sys.argv[1]
    pwd = sys.argv[2]
    db = sys.argv[3]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(usr, pwd, db), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    for city, state in session.query(City, State)\
                              .join(State, City.state_id == State.id)\
                              .order_by(City.id).all():
        print("{}: ({}) {}".format(state.name, city.id, city.name))
