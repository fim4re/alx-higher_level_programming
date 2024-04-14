#!/usr/bin/python3
""" Contains State class and Base"""
from sqlalchemy import Column, Integer, String, MetaData
from sqlalchemy.ext.declarative import declarative_base

my_meta_data = MetaData()
Base = declarative_base(metadata=my_meta_data)


class State(Base):
    """ Class with id and name of each state"""
    __tablename__ = 'states'
    id = Column(Integer, unique=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
