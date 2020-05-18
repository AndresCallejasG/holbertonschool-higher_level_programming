#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    result = None
    try:
        result = fct(*args)
    except Exception as error_msg:
        print("Exception: {}".format(error_msg), file=stderr)
    finally:
        return result
