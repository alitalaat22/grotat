#!/usr/bin/python3
def print_last_digit(number):
	if number > 0:
		las = number %10
		print("{:}".format(las), end='')
	elif number < 0:
		las = number % -10
		print("{:}".format(las * -1), end='')
	else:
		las = number
		print("{:}".format(las), end='')
	return las * -1
	