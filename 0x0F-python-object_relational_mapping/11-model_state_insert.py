#!/usr/bin/python3
""" adds the State object Louisian to the database """
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
    new_stat = State(name='Louisiana')
    sen.add(new_stat)
    new_inst = sen.query(State).filter_by(name='Louisiana').first()
    print(new_inst.id)
    sen.commit()
