#!/usr/bin/python3

def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_    string is None:
        return (0)
    dictn = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    N = 0
    for s in range(len(roman_string)):
        if dictn.get(roman_string[s], 0) == 0:
            return (0)

        if (s != (len(roman_string) - 1) and
                dictn[roman_string[s]] < dictn[rom    an_string[s + 1]]):
                N += dictn[roman_string[s]] * -1

        else:
            N += dictn[roman_string[s]]
    return (N)
