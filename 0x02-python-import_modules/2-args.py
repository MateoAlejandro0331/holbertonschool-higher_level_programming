#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    lens = len(argv)
    if lens == 1:
        print(f"{len - 1} arguments.")
    else:
        print(f"{lens - 1} arguments:")
        for i in range(1, lens):
            print(f"{i}: {argv[i]}")
