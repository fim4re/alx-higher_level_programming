#!/usr/bin/python3
""" """
import sys
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:/{}'.
                           format(sys.argv[1], sys.argv[2], sys.argv[3]))
    #create session
    Session = sessionmaker(bind=engine)
    sen = Session()
    # new object
    new_State = State(name='California')
    new_City = City(name='San Francisco')
    new_State.cities.append(new_City)
    # add
    sen.add(new_State)
    sen.add(new_City)
    sen.commit()
