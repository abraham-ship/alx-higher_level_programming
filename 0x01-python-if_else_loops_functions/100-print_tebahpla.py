#!/usr/bin/python3
for i in range(ord("Z"), ord("A") - 1, -1):
    if i % 2 == 0:
        print("{:c}".format(i + 32), end='')
    else:
        print("{:c}".format(i), end='')
