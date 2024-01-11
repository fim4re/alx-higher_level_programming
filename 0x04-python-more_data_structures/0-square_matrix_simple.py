#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    s = []
    for n in matrix:
        s.append([i**2 for i in n])
    return s
