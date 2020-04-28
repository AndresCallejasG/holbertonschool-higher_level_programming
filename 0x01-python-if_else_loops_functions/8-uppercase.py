#!/usr/bin/python3
def uppercase(str):
    i = 0
    for i in range(len(str)):
        c_val = ord(str[i])
        if c_val >= 97 and c_val <= 122:
            c_val = c_val - 32
        print("{}".format(chr(c_val)), end="")
    print("")
