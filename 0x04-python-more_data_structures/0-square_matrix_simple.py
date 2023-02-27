#!/usr/bin/python3

""" computes the square value of all integers of a matrix """

def square_matrix_simple(matrix=[]):
    return ([list(map(lambda x: x * x, r)) for r in matrix])
