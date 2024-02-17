#!/usr/bin/python3
def print_last_digit(number):
    if number > 0 or number == 0:
        las = number % 10
        print("{:}".format(las), end='')
        return las
    else:
        las = number % -10
        print("{:}".format(las * -1), end='')
        return las * -1
