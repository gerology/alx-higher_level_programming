#!/usr/bin/python3

def only_diff_elements(set_1, set_2):
    new = []
    new = list(set_1) + list(set_2)
    new = sorted(set(new))
    for item in set_1:
        if item in set_2:
            new.remove(item)

    return (new)
