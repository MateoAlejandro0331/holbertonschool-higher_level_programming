#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
            newlist = list(a_dictionary)
            max_value = max(newlist)
            return max_value
    else:
        return None
