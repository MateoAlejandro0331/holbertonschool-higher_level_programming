def print_reversed_list_integer(my_list=[]):
    lens = len(my_list) - 1
    for i in range(lens, -1, -1):
        print(my_list[i])
