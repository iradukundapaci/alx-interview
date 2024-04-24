#!/usr/bin/python3
"""Rotate 2d matrix"""


def rotate_2d_matrix(matrix) -> None:
    """
    Rotate 2d matrix 90 degrees clockwise

    args:
        matrix: matrix to rotate

    return: none
    """
    matrix.reverse()

    for row in range(len(matrix)):
        for column in range(len(matrix)):
            if row < column:
                matrix[row][column], matrix[column][row] = (
                    matrix[column][row],
                    matrix[row][column],
                )
