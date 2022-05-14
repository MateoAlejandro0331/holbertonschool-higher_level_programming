#!/usr/bin/env python3
def print_last_digit(number):
    last = str(number)
    digit = int(last[-1])
    print(f"{digit}", end="")
    return digit
