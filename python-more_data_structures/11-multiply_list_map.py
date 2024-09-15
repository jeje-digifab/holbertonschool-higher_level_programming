#!/usr/bin/python3
"""
This script contains utility functions for basic arithmetic operations.
"""


def multiply_list_map(my_list=[], number=0):
    new_list = my_list.copy()
    new_list = list(map(lambda i: i * number, new_list))
    return (new_list)
