#!/usr/bin/python3
import random
number = random.randint(-10, 10)
if number > 0:
    print("{} is positive".format(number), end="")
elif number == 0:
    print("{} is Zero".format(number), end="")
else:
    print("{} is negative".format(number), end="")
print(end="")
