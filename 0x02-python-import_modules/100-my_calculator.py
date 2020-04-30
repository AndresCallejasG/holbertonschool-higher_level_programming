#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import mul, div, add, sub

    av = sys.argv
    argc = len(av)

    if argc != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    else:
        a = int(av[1])
        b = int(av[3])

    if av[2] == "*":
        print("{:d} + {:d} = {:d}".format(a, b, mul(a, b)))
    elif av[2] == "/":
        print("{:d} - {:d} = {:d}".format(a, b, div(a, b)))
    elif av[2] == "+":
        print("{:d} * {:d} = {:d}".format(a, b, add(a, b)))
    elif av[2] == "-":
        print("{:d} / {:d} = {:d}".format(a, b, sub(a, b)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
