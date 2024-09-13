def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a given divisor and returns
    a new matrix with the results rounded to 2 decimal places.

    Parameters:
    matrix (list of lists of int/float): A matrix (list of lists) where
    each sub-list represents a row of the matrix. All elements of the matrix
    must be integers or floats.
    div (int/float): The divisor by which each element of the matrix
    is divided. Must be a non-zero number.

    Returns:
    list of lists of float: A new matrix where each element is the result
    of dividing the corresponding element of the input matrix by `div`,
    rounded to two decimal places.

    Raises:
    TypeError: If `matrix` is not a list of lists, or if any element
    in `matrix` is not an integer or float, or if `div` is not a number.
    TypeError: If the rows of `matrix` do not all have the same size.
    ZeroDivisionError: If `div` is zero.
    """

    # Check if matrix is a list of lists
    if not isinstance(matrix, list) or \
            not all(isinstance(row, list) for row in matrix):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")

    # Check if all elements in matrix are integers or floats
    if not all(isinstance(el, (int, float)) for row in matrix for el in row):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")

    # Check if all rows in matrix have the same size
    row_length = len(matrix[0])
    if not all(len(row) == row_length for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    # Check if div is a number and not zero
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Perform division and round results
    result = []
    for row in matrix:
        divided_row = [round(el / div, 2) for el in row]
        result.append(divided_row)

    return result
