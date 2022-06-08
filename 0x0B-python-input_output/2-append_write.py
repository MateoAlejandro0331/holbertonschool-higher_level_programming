#!/usr/bin/python3
"""
    Funtion to read a file
"""


def append_write(filename="", text=""):
    """My Funtion"""
    with open(filename, 'a', encoding='utf-8') as file:
        file.write(text)
        return len(text)
