#!/usr/bin/python3


def safe_print_division(a, b):
    """
       Args:
           a(int) - integer numerator
           b(int) - integer denominator
       Return:
           returns the result of division between the 2 integers
    """
    try:
        sum = 0
        sum = a / b
    except (TypeError, ValueError, ZeroDivisionError):
        sum = None
    finally:
        print("Inside result: {}".format(sum))
        return (sum)
