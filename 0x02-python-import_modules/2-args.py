#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    lens = len(argv)
    if lens == 1:
        print("0 arguments.")
    elif lens == 1:
        print("1 argument:")
        print("1: " + argv[1])
    elif:
        print(f"{lens - 1} arguments:")
        for i in range(1, lens):
            print(f"{i}: {argv[i]}")
