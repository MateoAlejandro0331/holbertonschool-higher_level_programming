#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    newlist = []
    lista = list(tuple_a)
    listb = list(tuple_b)
    if len(lista) < 2:
        lista.append(0)
    if len(listb) < 2:
        listb.append(0)
    if len(lista) == 0:
        return(tuple_b)
    if len(listb) == 0:
        return(tuple_a)
    aux = lista[0] + listb[0]
    newlist.append(aux)
    aux = lista[1] + listb[1]
    newlist.append(aux)
    newtuple = tuple(newlist)
    return(newtuple)
