#!/usr/bin/python3
"""
This script contains utility functions for basic arithmetic operations.
"""


class MyList(list):
    """
    This class inherits from list and adds a new method to sort the list.
    """

    def print_sorted(self):

        print ("{:d}".format(sorted(self)))
        return super("{:d}".format(sorted(self)))
