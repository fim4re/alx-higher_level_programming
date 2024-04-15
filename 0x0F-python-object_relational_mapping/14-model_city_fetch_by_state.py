#!/usr/bin/python3
""" file similar to model_state named model_city"""
import sys
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    # create session
    Session = sessionmaker(bind=engine)
    session = Session()
    for inst in (session.query(State.name, City.id, City.name)
                     .filter(City.state_id == State.id)):
        print("{}: ({}) {}".format(state.name, city.id, city.name))
