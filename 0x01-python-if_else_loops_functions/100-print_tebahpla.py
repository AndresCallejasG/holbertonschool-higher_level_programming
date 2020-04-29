#!/usr/bin/python3
for i in range(122, 96, -1):
    letter = i - 32 * (i % 2)
    print("{}".format(chr(letter)), end="")
