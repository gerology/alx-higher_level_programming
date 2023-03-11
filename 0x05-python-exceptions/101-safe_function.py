#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        f = fct(*args)
    except (TypeError, ZeroDivisionError, ValueError):
        print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
        return (None)
    return (f)
