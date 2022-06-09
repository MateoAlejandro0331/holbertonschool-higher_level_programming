#!/usr/bin/python3
"""
    Function that returns a list of lists of integers
    representing the Pascal triangle
"""


def pascal_triangle(n):
    """
        My list - pascal triangle
        rows - rows to create the triangle
    """
    mylist = []
    rows = []
    for i in range(n):
        rows = [1]
        if i > 0:
            for j in range(i):
                rows.append(sum(mylist[-1][j:j+2]))
        mylist.append(rows)
    return mylist
