#!/usr/bin/python3

def best_score(a_dictionary):
    if not isinstance(a_dictionary, dict) or len(a_dictionary) == 0:
        return None

    g = list(a_dictionary.keys())[0]
    s = 0
    b = a_dictionary[g]
    for k, v in a_dictionary.items():
        if v > b:
            b = v
            g = k
    return (g)
