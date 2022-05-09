#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    lens = len(my_list) - 1
    if idx < 0:
        return(my_list)
    if idx > lens:
        return(my_list)
    for i in range(lens):
        if i == idx:
            my_list[i] = element
            return(my_list)
