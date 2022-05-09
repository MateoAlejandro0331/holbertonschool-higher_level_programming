def element_at(my_list, idx):
    lens = len(my_list)
    if idx < 0:
        return(None)
    if idx > lens - 1:
        return(None)
    for i in range(lens - 1):
        if i == idx:
            return(my_list[i])
