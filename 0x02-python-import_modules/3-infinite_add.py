#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    add = 0
    lens = len(argv)
    for i in range(1, lens):
        add += int(argv[i])
    print(f"{add}")
