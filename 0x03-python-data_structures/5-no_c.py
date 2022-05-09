#!/usr/bin/python3
def no_c(my_string):
    if my_string:
        new = my_string.replace("c", "")
        new = new.replace("C", "")
        return(new)
