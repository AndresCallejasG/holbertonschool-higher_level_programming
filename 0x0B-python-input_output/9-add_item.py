#!/usr/bin/python3
""" Input/Output project
"""


import sys

save_to_json_file = __import__('7-save_to_json_file').save_to_json_file

load_from_json_file = __import__('8-load_from_json_file').load_from_json_file

p_list = []
try:
    p_list = load_from_json_file('add_item.json')
    p_list.extend(sys.argv[1:])

except FileNotFoundError:
    p_list = sys.argv[1:]

finally:
    save_to_json_file(p_list, 'add_item.json')
