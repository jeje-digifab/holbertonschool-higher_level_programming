#!/usr/bin/python3
"""Module compiled with python3"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a given number.

    Args:
        matrix (list): A list of lists containing integers or floats.
        div (int or float): The number by which to divide each element
        of the matrix.

    Returns:
        list: A new matrix where each element is the result of
        dividing the corresponding element of the original matrix by div.

    Raises:
        TypeError: If matrix is not a list of lists of integers
        or floats, or if each row of the matrix does not have the
        same size, or if div is not a number.
        ZeroDivisionError: If div is equal to zero.

    Example:
        matrix = [
            [1, 2, 3],
            [4, 5, 6]
        ]
        print(matrix_divided(matrix, 3))
        # Output: [[0.33, 0.67, 1.0], [1.33, 1.67, 2.0]]
    """
    # Vérifier que la matrice est valide
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if not matrix:
        raise TypeError("matrix cannot be empty")
    if not all(isinstance(elem, (int, float)) for row in matrix for elem in row):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    # Vérifier que div est valide
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Créer une nouvelle matrice pour stocker les résultats
    new_matrix = []
    for row in matrix:
        # Vérifier que la ligne contient au moins un élément
        if not row:
            raise TypeError("Each row of the matrix must have at least one element")
        new_row = []
        for elem in row:
            new_row.append(round(elem / div, 2))
        new_matrix.append(new_row)

    return new_matrix


if __name__ == "__main__":
    main()
