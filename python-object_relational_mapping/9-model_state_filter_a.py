#!/usr/bin/python3
"""
This script connects to a MySQL database, retrieves and prints all State
records from the `states` table using SQLAlchemy, ordered by their IDs,
that contain the letter 'a' in their name.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def main():
    """
    Establishes a connection to the MySQL database using SQLAlchemy,
    creates all tables defined in the `Base` metadata if they do not exist,
    and retrieves all `State` records containing the letter 'a' in their name,
    ordered by ID, to display them.
    """
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)

    session = Session()
    # HERE: no SQL query, only objects!
    for state in session.query(State).order_by(State.id).filter(State.name.like("%a%")).all():
        print("{}: {}".format(state.id, state.name))
    session.close()


if __name__ == "__main__":
    main()
