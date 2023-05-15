def print_last_digit(number):
    temp = abs(number) % 10
    print("{}".format(temp), end='')
    return temp
