#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
flag = 0
str = "Last digit of"
str5 = "and is greater than 5"
str0 = "and is 0"
str6 = "and is less than 6 and not 0"

if number < 0:
    flag = 1
    number = number * -1
digit = number % 10
if flag:
    digit = digit * -1
    number = number * -1
if digit > 5:
    print("{} {:d} is {:d} {}".format(str, number, digit, str5))
elif digit == 0:
    print("{} {:d} is {:d} {}".format(str, number, digit, str0))
else:
    print("{} {:d} is {:d} {}".format(str, number, digit, str6))
