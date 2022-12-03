#!/usr/bin/python3
def print_last_digit(number):
    while True:
        value = number % 10
        print(value, end="")
        return value
