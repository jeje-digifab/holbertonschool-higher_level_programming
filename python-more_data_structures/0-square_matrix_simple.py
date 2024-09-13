#!/usr/bin/python3
"""
This script contains utility functions for basic arithmetic operations.
"""


def square_matrix_simple(matrix=[]):
    """
    Return a new matrix where each element is the square of the original.

    Args:
        matrix (list): A 2D list where each inner list represents a row
                       of the matrix. Default is an empty list.

    Returns:
        list: A new 2D list where each element is the square of the
              corresponding element in the input matrix.
    """

    for i in matrix:
        result = []
        for row in matrix:
            squared_row = [el ** 2 for el in row]
            result.append(squared_row)
        return (result)
