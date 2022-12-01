#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lastNum = abs(number) % 10
def last(n):
	"""determine if number is greater than 5, equal to 0, and less than 6 not 0"""
	if n > 5:
		greater = 'and is greater than 5'
		return greater
	elif n == 0:
		equalto0 = 'and is 0'
		return equalto0
	elif n < 6 & n != 0:
		less6 = 'and is less than 6 and not 0'
		return less6
stmt = last(lastNum)
print("Last digit of {0} is {1} {2}".format(number, lastNum, stmt))
print("\n")
