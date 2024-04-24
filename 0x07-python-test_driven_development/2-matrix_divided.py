#!/usr/bin/python3
""" 
    divides all elements of a matrix
"""


def matrix_divided(matrix, div):
    """divides all elements of a matrix
    Args:
        matrix (:obj:`list` of :obj:`list` of :obj:`int` or :obj:`float`):
            list of lists of integers or floats
        div (int or float): divisor
    Returns:
        a new matrix containing the quotients
    Raises:
        TypeError: if matrix elements are neither int nor float,
            if matrix rows are not the same size
        ZeroDivisionError: if dividing by zero
    """
    if not isinstance(matrix, list) or len(matrix) == 0 or not matrix[0]:
        raise TypeError("matrix must be a matrix (list of lists) " +
                        "of integers/floats")

    for row in matrix:
        if len(row) == 0:
            raise TypeError("matrix must be a matrix (list of lists) " +
                            "of integers/floats")
        for x in row:
            if type(x) is not int and type(x) is not float:
                raise TypeError("matrix must be a matrix (list of lists) " +
                                "of integers/floats")

    len_rows = []
    for row in matrix:
        len_rows.append(len(row))
    if not all(elem == len_rows[0] for elem in len_rows):
        raise TypeError("Each row of the matrix must have the same size")

    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = [[round(x / div, 2) for x in row] for row in matrix]

    return new_matrix
