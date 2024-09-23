#!/usr/bin/python3
"""
This script contains utility functions for basic arithmetic operations.
"""


def lookup(obj):
    """
    This function takes an object as input and returns a list of all the
    valid attributes and methods associated with the object.
    """
    return dir(obj)
