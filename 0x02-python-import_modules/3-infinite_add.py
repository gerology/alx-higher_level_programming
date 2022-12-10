#!/usr/bin/python3
if __name__ =="__main__":
    import sys
L = len(sys.argv)
sum = 0
n = 1
if L < 2:
    print("0")
else:
    while L >= 2 and L > n:
        v = sys.argv[n]
        sum = sum + int(v)
        n = n + 1
    print(sum)
