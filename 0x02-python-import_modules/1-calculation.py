#!/usr/bin/python3
if __name__ == "__main__":

    from calculator_1 import add, sub, mul, div

    a = 10
    b = 5

    total = add(a, b)
    difference = sub(a, b)
    product = mul(a, b)
    diff2 = div(a, b)

    print("{} + {} = {}".format(a, b, total), end='\n')
    print("{} - {} = {}".format(a, b, difference), end='\n')
    print("{} * {} = {}".format(a, b, product), end='\n')
    print("{} / {} = {}".format(a, b, diff2), end='\n')
