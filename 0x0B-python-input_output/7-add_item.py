#!/usr/bin/python3
"""import module"""
import os.path
from sys import argv
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


if __name__ == "__main__":
    lens = len(argv)
    mylist = []
    if os.path.exists("add_item.json"):
        obj = load_from_json_file("add_item.json")
        for i in range(1, lens):
            obj.append(argv[i])
        save_to_json_file(obj, "add_item.json")
    else:
        for i in range(1, lens):
            mylist.append(argv[i])
        save_to_json_file(mylist, "add_item.json")
