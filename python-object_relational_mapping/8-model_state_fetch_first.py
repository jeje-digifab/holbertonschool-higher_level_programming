#!/usr/bin/python3
"""
This script connects to a MySQL database, retrieves and prints the first
State record from the `states` table using SQLAlchemy. If no records are
found, it prints 'Nothing'.
"""


import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def main():
    """
    Establishes a connection to the MySQL database using SQLAlchemy,
    creates all tables defined in the `Base` metadata if they do not exist,
    and retrieves the first `State` record ordered by ID to display it.
    If no `State` records are found, it prints 'Nothing'.
    """

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)

    session = Session()
    # HERE: no SQL query, only objects!
    state = session.query(State).order_by(State.id).first()
    if state:
        print("{}: {}".format(state.id, state.name))
    else:
        print("{}".format("Nothing"))

    session.close()


if __name__ == "__main__":
    main()
