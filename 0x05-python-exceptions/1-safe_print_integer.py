#!/usr/bin/python3


def safe_print_integer(value):
    """
       args:
            value = value to be printed
       Return:
           returns True if printed correctly
    """
    try:
        print("{:d}".format(value))
    except ValueError:
        return (TypeError, ValueError)
    else:
        return True
