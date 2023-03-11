#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    """ print an integer

       Args:
            value - value to be printed
       Return:
            returns True if correctly printed else False
    """
    try:
        print("{:d}".format(value))
    except (ValueError, TypeError):
        print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
        return False
    return True
