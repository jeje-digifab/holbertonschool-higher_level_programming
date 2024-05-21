#!/usr/bin/python3
"""Module compiled with python3"""


def say_my_name(first_name, last_name=""):
    """
    Fonction qui imprime "My name is <first name> <last name>"
    si first_name et last_name sont des chaînes de caractères.
    Sinon, une exception TypeError est levée.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {:s} {:s}".format(first_name, last_name))


if __name__ == "__main__":
    main()
