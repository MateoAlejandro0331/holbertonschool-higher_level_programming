#!/usr/bin/python3
def element_at(my_list, idx):
    lens = len(my_list) - 1
    if idx < 0:
        return(None)
    if idx > lens:
        return(None)
    for i in range(lens):
        if i == idx:
            return(my_list[i])
