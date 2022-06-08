#!/usr/bin/python3
def to_upper(str):
    s= ""
    for c in str:
        if ord(c) == 32:
            s += c
        elif 64 < ord(c) < 91:
            s += chr(ord(c) - 32)
        else:
            s += c
    print("{}".format(s))
