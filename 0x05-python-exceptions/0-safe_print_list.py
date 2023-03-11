#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    """
        args:
            my_list - list to print from
            x - number of elements to print
    """
    sum = 0
    for d in range(x):
        try:
            print("{}".format(my_list[d]), end="")
            sum += 1
        except IndexError:
            pass
    print("")
    return (sum)
