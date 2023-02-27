#!/usr/bin/python3

def weight_average(my_list=[]):
    if len(my_list) == 0:
        return (0)
    num = 0
    den = 0
    agv = 0
    for cluster in my_list:
        num += cluster[0] * cluster[1]
        den += cluster[1]
    avg = num / den
    return (avg)
