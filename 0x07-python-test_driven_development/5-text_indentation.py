#!/usr/bin/python3
"""

Funtion to print a new line by patterns

"""


def text_indentation(text):
    """
    Funtion to print a new line by patterns
    """
    newline = ""
    if type(text) is not str:
        raise TypeError("text must be a string")
    newtext = text.split()
    for word in newtext:
        newline += word + " "
        slen = len(newline)
        """print(newline[slen - 2:-1])"""
        if newline[slen - 2:-1] == "." or newline[slen - 2:-1] == "?" \
                or newline[slen - 2:-1] == ":":
            newline = newline.strip()
            print(newline)
            print()
            newline = ""
    newline = newline.strip()
    print(newline, end="")
