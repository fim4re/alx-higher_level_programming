#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    s = []
    for l in matrix:
        s.append([i**2 for i in l])
    return s
