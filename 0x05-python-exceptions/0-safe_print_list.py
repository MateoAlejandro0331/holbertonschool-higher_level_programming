#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        for idx, i in enumerate(my_list[:x]):
            print(i, end="")
        print()
        return idx + 1
    except IndexError:
        return idx + 1
