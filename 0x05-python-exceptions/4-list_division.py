#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result_list = []
    result = 0
    for i in range(list_length):
        try:
            result = my_list_1[i] / my_list_2[i]
        except IndexError:
            print("out of range")
        except ZeroDivisionError:
            print("division by 0")
        except TypeError:
            print("wrong type")
        finally:
            result_list.append(result)
        result = 0
    return result_list
