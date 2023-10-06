#!/usr/bin/env python3

# Exercise 3. Paramètres à l’envers (Print parameters in reverse)

import sys

def check_empty():
	try:
		if sys.argv[1]:
			pass
	except IndexError:
		print("error.")
		exit()

def reverse_arguments(arguments, reversed_arguments):
	for item in arguments[:0:-1]: # we could have used the reverse() built in function instead
		reversed_arguments.append(item)
	return reversed_arguments


# 1. Handling Errors 
check_empty()

# 2. Parsing 
arguments = sys.argv
reversed_arguments = []

# 3. Resolution
reversed_arguments = reverse_arguments(arguments, reversed_arguments)

# 4. Display 
print(*reversed_arguments, sep="\n")