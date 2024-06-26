#!/usr/bin/python3
""" prints the first State from hbtn_0e_6_usa"""
import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    # create session
    Session = sessionmaker(bind=engine)
    session = Session()
    inst = session.query(State).first()
    if inst is None:
        print("Nothing")
    else:
        print(inst.id, inst.name, sep=": ")
