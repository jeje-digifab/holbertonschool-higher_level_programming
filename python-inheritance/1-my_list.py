#!/usr/bin/python3
"""
This script contains utility functions for basic arithmetic operations.
"""


class MyList(list):
    """
    MyList is a subclass of the built-in list that adds a method to print
    a sorted version of the list without modifying the original order.

    Methods:
    --------
    print_sorted():
        Prints a sorted version of the list while preserving the original list.
    """

    def print_sorted(self):
        """
        Prints a sorted version of the list.
        The original list remains unchanged.
        """
        sorted_list = sorted(self)
        print(sorted_list)
