#!/usr/bin/python3
"""
This script connects to a MySQL database, retrieves and prints the State
record with a specified name from the `states` table using SQLAlchemy.
If no record is found, it prints 'Not found'.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def main():
    """
    Establishes a connection to the MySQL database using SQLAlchemy,
    creates all tables defined in the `Base` metadata if they do not exist,
    and retrieves the `State` record with a name matching the provided
    filter argument. If the state is found, it prints its ID; otherwise,
    it prints 'Not found'. Exits with an error if the wrong number of
    arguments is provided.
    """
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    try:
        if len(sys.argv) < 5 or len(sys.argv) >= 6:
            raise IndexError("Expected exactly 5 arguments")
        filter = sys.argv[4]

    except IndexError as e:
        print(e)
        sys.exit(1)

    Session = sessionmaker(bind=engine)

    session = Session()
    # HERE: no SQL query, only objects!
    state = session.query(State).filter_by(name=filter).one_or_none()

    if state is None:
        print("Not found")
    else:
        print("{}".format(state.id))

    session.close()


if __name__ == "__main__":
    main()
