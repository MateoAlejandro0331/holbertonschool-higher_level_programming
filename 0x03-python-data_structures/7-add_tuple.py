#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    newlist = []
    lista = list(tuple_a + (0, 0))
    listb = list(tuple_b + (0, 0))
    aux = lista[0] + listb[0]
    newlist.append(aux)
    aux = lista[1] + listb[1]
    newlist.append(aux)
    newtuple = tuple(newlist)
    return(newtuple)
