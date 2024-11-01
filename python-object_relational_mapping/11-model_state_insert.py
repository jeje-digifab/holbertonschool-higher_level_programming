#!/usr/bin/python3
"""
This script connects to a MySQL database using SQLAlchemy, adds a new State
record named "Louisiana" to the `states` table, and commits the change.
If the table does not exist, it creates all tables defined
in the `Base` metadata.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def main():
    """
    Establishes a connection to the MySQL database using SQLAlchemy,
    creates all tables defined in the `Base` metadata if they do not exist,
    adds a new `State` record with the name "Louisiana" to the `states` table,
    commits the transaction, and closes the session.

    Exits with an error if the required command-line arguments
    are not provided.
    """
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)

    session = Session()
    # HERE: no SQL query, only objects!

    louisiana = State(name="Louisiana")
    session.add(louisiana)
    session.commit()

    session.close()


if __name__ == "__main__":
    main()
