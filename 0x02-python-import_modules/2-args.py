#!/usr/bin/python3
import sys

L = len(sys.argv)-1
if L == 0:
    print("{} arguments.".format(L))
elif L == 1:
    print("{} argument:".format(L))
    print("{}: {}".format((L), sys.argv[L]))
elif L > 1:
    print("{}: arguments:".format(L))
    arg = 1
    while L >= arg:
        print("{}: {}".format(arg, sys.argv[arg]))
        arg = arg + 1
