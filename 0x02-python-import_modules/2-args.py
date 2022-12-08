#!/usr/bin/python3
if __name__ == "__main__":
    import sys

L = len(sys.argv)-1
if L == 0:
    print("0 arguments.")
elif L == 1:
    print("1 argument:")
    print("{}: {}".format((L), sys.argv[L]))
else:
    print("{}: arguments:".format(L))
    arg = 1
    while L + 1 > arg:
        print("{}: {}".format(arg, sys.argv[arg]))
        arg = arg + 1
