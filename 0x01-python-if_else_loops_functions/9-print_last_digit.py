#!/usr/bin/python3
def print_last_digit(number):
    digit = 0
    if number > 0:
        digit = number % 10
    elif number < 0:
        digit = number % -10
        digit = digit * -1
    print("{:d}".format(digit), end="")
    return digit
