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
    
    for arg in range(L):
        print("{}: {}".format(arg + 1, sys.argv[arg + 1]))
