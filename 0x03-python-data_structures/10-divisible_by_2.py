#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    l = len(my_list)
    new_list = []
    for item in my_list:
        if item % 2 ==  0 and item <= l:
            new_list.append(True)
        else:
            new_list.append(False)
    return (new_list)
