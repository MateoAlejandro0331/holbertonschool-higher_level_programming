#!/usr/bin/python3
def search_replace(my_list, search, replace):
    copy = my_list.copy()
    for idx, i in enumerate(copy):
        if i == search:
            copy[idx] = replace
    return copy
