#!/usr/bin/python3

def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    l = len(my_list)
    comp = 0
    i = 0
    while i < l:
        if my_list[i] > comp:
            comp = my_list[i]
        i = i + 1
    return (comp)
