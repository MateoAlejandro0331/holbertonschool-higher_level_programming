#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        newlist = a_dictionary.values()
        max_value = max(newlist)
        for key, value in a_dictionary.items():
            if value == max_value:
                return key
    else:
        return None
