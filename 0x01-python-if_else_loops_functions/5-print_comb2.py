#!/usr/bin/python3
for num in range(00, 100):
    print("{:02}".format(num), end='\n' if num == 99 else ", ")
