#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    for element in range(len(tuple_a)):
        if tuple_a[element] == None:
            tuple_a[element] = 0
        element = element + 1

    for item in range(len(tuple_b)):
        if tuple_b[item] == None:
            tuple_b[item] = 0
        element = element + 1

    sum =((tuple_a[0] + tuple_b[0]), (tuple_a[1] +tuple_b[1]))
    return(sum)
