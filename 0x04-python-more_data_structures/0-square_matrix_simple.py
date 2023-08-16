#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    square_matrix = []
    for row in matrix:
        square_row = []
        for element in row:
            sq_element = element ** 2
            square_row.append(sq_element)
        square_matrix.append(square_row)
    return square_matrix
