#!/usr/bin/python3
""" changes the name of a State object from the database"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),)
    # create sesson
    Session = sessionmaker(bind=engine)
    sen = Session()

    stat = sen.query(State).filter_by(id=2).first()
    stat.name = "New Mexico"
    sen.commit()
