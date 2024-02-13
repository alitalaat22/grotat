#!/usr/bin/python3
for num in range(0, 100):
	if num == 99:
		print("{:d}" .format(num) , end='\n')
	print("{:d}" .format(num) .zfill(2), end=', ')
	
			