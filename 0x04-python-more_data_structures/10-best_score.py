#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        for i in a_dictionary:
            value = a_dictionary.get(i)
            for j in a_dictionary:
                aux = a_dictionary.get(j)
                if aux > value:
                    value = aux
            return value
    else:
        return None
