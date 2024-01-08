#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix:
        return None
    else:
        for y in matrix:
            for z in y:
                print("{:d}".format(z), end=' ' if z != y[-1] else '')
            print()
