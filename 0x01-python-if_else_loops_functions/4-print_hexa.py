#!/usr/bin/python3
for num in range(0, 100):
	print("{:d}" .format(num).zfill(2), end=', ')
	if num == 99:
		print("{:d}".format(num), end='\n')