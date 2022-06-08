#!/usr/bin/python3
"""
    Funtion to read a file
"""


def read_file(filename=""):
    """My Funtion"""
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
        print(content, end="")
