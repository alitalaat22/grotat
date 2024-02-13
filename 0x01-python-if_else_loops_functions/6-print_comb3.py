#!/usr/bin/python3
for num in range(0, 10):
    for nums in range(num+1, 10):
        if num == 8 and nums == 9:
            print("{:d}{:d}".format(num, nums))
        else:
            print("{:d}{:d}".format(num, nums), end=', ')
