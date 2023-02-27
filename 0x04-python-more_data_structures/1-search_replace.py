#!/usr/bin/python3

def search_replace(my_list, search, replace):
    copy = my_list.copy()
    t = 0
    for g in range(len(copy)):
        if copy[g] == search:
            copy[g] = replace
    return (copy)
