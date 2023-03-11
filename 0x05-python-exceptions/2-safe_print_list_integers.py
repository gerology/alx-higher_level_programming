#!/usr/bin/python3


def safe_print_list_integers(my_list=[], x=0):
    """
        Args:
             my_list - list to print from

             x = number of elements to print
        Return:
             returns the real number of integers printed
    """
    sum = 0
    for d in range(0, x):
        try:
            if isinstance(d, int):
                print("{:d}".format(my_list[d]), end="")
                sum += 1
        except (TypeError, ValueError):
            pass
    print("")
    return (sum)
