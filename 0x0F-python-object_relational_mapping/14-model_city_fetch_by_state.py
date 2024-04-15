#!/usr/bin/python3
""" file similar to model_state.py named model_city.py"""
import sys
from model_state import Base, State
from model_city import City
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    # create session
    Session = sessionmaker(bind=engine)
    sen = Session()
    for inst in (sen.query(State.name, City.id, City.name) \
                 .filter(State.id == City.state_id)):
        print(inst[0] + ": (" + str(inst[1]) + ") " + inst[2])
