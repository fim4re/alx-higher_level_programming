#!/usr/bin/python3
""" file similar to model_state named model_city """

import sys
from model_state import State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    # create session
    Session = sessionmaker(bind=engine)
    session = Session()
    for state, city in session.query(State, City) \
                     .filter(City.state_id == State.id).order_by(City.id):
        # print city and state
        print("{}: ({}) {}".format(state.name, city.id, city.name))
