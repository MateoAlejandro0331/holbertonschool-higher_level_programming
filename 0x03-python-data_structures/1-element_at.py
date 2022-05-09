#!/usr/bin/python3
def element_at(my_list, idx):
    lens = len(my_list) - 1
    if idx < 0 or idx > lens:
        return(None)
    else:
        return(my_list[idx])
