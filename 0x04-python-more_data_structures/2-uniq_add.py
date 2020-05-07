#!/usr/bin/python3
def uniq_add(my_list=[]):
    add = 0
    my_set = set(my_list)
    for elem in my_set:
        add += elem
    return add
