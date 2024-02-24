#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for row in matrix:
        new = []
        for col in row:
            col = col * col
            new.append(col)
        new_matrix.append(new)
    return new_matrix
