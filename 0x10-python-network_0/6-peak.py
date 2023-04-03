#!/usr/bin/python3
# algorithm to find a peak in a list of unsorted integers.


def find_peak(list_of_integers):
    """ return the peak value in an unsorted list of integers."""
    if list_of_integers == []:
        return None

    size = len(list_of_integers)
    if size == 1:
        return list_of_integers[0]

    if size == 2:
        return max(list_of_integers)

    m = int(size / 2)
    p = list_of_integers[m]

    if p > list_of_integers[m - 1] and p > list_of_integers[m + 1]:
        return p
    elif p < list_of_integers[m - 1]:
        return find_peak(list_of_integers[:m])
    else:
        return find_peak(list_of_integers[m + 1:])
