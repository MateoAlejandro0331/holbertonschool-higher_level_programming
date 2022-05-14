#!/usr/bin/env
def print_last_digit(number):
    if number > 0:
        print(f"{number % 10}", end="")
        return number % 10
    else:
        number = number * -1
        print(f"{number % 10}", end="")
        return number % 10
