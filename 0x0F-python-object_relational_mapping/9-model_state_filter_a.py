#!/usr/bin/python3
""" lists all State objects that contain the letter a """
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
    for inst in sen.query(State).filter(State.name.like('%a%')):
        print(inst.id, inst.name, sep=": ")
