#!/usr/bin/python3

import hidden_4
import inspect


if __name__ == "__main__":
    names = [name for name, value in inspect.getmembers(hidden_4, inspect.isfunction) if not name.startswith("__")]

    names.sort()

    for name in names:
        print("{:s}".format(name))
