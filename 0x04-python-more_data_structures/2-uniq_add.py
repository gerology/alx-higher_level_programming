#!/usr/bin/python3

def uniq_add(my_list=[]):
    new = list(set(my_list))
    sum = 0
    for item in new:
        sum = sum + item
    return (sum)
