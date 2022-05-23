#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    aux = ""
    try:
        for i in range(x):
            aux = str(my_list[i])
            if aux.isdigit():
                print("{:d}".format(int(aux)), end="")
                count += 1
        print()
        return count
    except IndexError:
        raise IndexError
