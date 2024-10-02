#!/usr/bin/python3
"""
This script contains utility functions for basic arithmetic operations.
"""


def pascal_triangle(n):
    """
    Generates Pascal's triangle up to the nth row.

    Args:
        n (int): The number of rows of Pascal's triangle to generate.

    Returns:
        list of lists: A list of lists where each inner list represents a row
                       of Pascal's triangle.
                       Returns an empty list if n <= 0.
    """

    
    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
        row.append(1)
        triangle.append(row)
    return triangle
