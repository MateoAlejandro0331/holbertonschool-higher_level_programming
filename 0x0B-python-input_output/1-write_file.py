#!/usr/bin/python3
"""
    Funtion to write and create a file
"""


def write_file(filename="", text=""):
    """My Funtion"""
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(text)
        return len(text)
