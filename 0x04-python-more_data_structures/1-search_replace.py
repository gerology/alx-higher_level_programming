#!/usr/bin/python3

def search_replace(my_list, search, replace):
    copy = my_list.copy()
    for item in my_list:
        if item == search:
            ind = my_list.index(item)
            copy[ind] = replace
    return (copy)
