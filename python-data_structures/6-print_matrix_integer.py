#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    """
    Prints the elements of a matrix.

    Each element in the matrix is separated by a space, and each row
    is printed on a new line.

    Args:
        matrix (list of lists of int): A 2D list (matrix) where each inner
        list represents a row of integers.
    """
    for row in matrix:
        """
        Initialize a list to store the string representations of the elements
        """
        row_elements = []

        """
        Convert each element in the row to a string and add to the list
        """
        for elem in row:
            row_elements.append("{:d}".format(elem))

        """
        Join the elements with a space and print the result
        """
        print(" ".join(row_elements))
