#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys
opera = {"+": add, "-": sub, "*": mul, "/": div}

if len(sys.argv) - 1 != 3:
    print("Usage: ./100-my_calculator.py <a> <operator> <b>")
    exit(1)
elif sys.argv[2] not in list(opera.keys()):
    print("Unknown operator. Available operators: +, -, * and /")
    exit(1)
else:
    a = int(sys.argv[1])
    b = int(sys.argv[3])
    print("{} {} {} = {}".format(a, sys.argv[2], b, opera[sys.argv[2]](a, b)))
    exit(0)

