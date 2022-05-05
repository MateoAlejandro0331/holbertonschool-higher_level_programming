#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    lens = len(argv)
    if lens == 1:
        print("0 arguments.")
    else:
        print(f"{lens - 1} arguments:")
        for i in range(1, lens):
            print(f"{i}: {argv[i]}")
