#!/usr/bin/python3
def uppercase(str):
    upper = ""
    for i in str:
        if ord(i) >= 97 and ord(i) <= 122:
            upper += chr(ord(i) - 32)
        elif ord(i) >= 65 and ord(i) <= 90:
            upper += chr(ord(i))
        else:
            upper += chr(ord(i))
    print(upper)
