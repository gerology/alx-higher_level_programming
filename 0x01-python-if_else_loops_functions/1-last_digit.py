#!/usr/bin/python3
import random
import sys
number = random.randint(-10000, 10000)

if number < 0:
    lastNum = number % -10
else:
    lastNum = number % 10


def last(n):
    """determine the state of a number with conditions"""
    if n > 5:
        greater = "and is greater than 5"
        return greater
    elif n == 0:
        equalto0 = "and is 0"
        return equalto0
    elif n < 6 and n != 0:
        less6 = "and is less than 6 and not 0"
        return less6


stmt = last(lastNum)
print("Last digit of {} is {} {}".format(number, lastNum, stmt), end="")
print("\n")
