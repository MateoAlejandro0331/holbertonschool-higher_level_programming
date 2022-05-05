#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    lens = len(sys.argv)
    if lens == 1:
        print("0 arguments.")
    else:
        print(f"{lens - 1} arguments:")
        for i in range(1, lens):
            print(f"{i}: {sys.argv[i]}")
