#!/usr/bin/python3
"""
Script that takes in the name of a state as an argument and lists
all cities of that state, using the database hbtn_0e_4_usa
"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Integer, String


Base = declarative_base()


class State(Base):
    __tablename__ = 'states'
    id = Column("id", Integer, primary_key=True,
                nullable=False, autoincrement=True)
    name = Column("name", String(128), nullable=False)
