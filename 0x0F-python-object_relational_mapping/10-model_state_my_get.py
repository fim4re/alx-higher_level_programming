#!/usr/bin/python3
""" prints the State object with the name passed as argument """
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    # create session
    Session = sessionmaker(bind=engine)
    sen = Session()
    inst = sen.query(State).filter(State.name == (sys.argv[4],))
    try:
        print(inst[0].id)
    except IndexError:
        print("Not found")
