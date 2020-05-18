#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    printed_cnt = 0
    try:
        for elem in range(x):
            print("{:d}".format(my_list[elem]), end="")
            printed_cnt += 1
    except IndexError:
        pass
    print()
    return printed_cnt
