#!/usr/bin/env python3

# Exercise 4. Suite de Fibonacci (Fibonacci Sequence)

import sys

def check_empty(argument):
    if not argument:
        print(-1)
        sys.exit()

def int_check(argument):
	try:
		if isinstance(int(argument), int):
			pass
	except ValueError:
		print(-1)
		exit()

def generate_fibonacci(argument, fibonacci): # we create the Fibonacci sequence till our arugument number
	i = 0
	while fibonacci[i] < int(argument):
		fibonacci.append(fibonacci[i] + fibonacci[i + 1])
		i += 1
	return fibonacci

def return_previous(argument, fibonacci): # return the previous element in the Fibonacci sequence
	for i in range(0, len(fibonacci)):
		if fibonacci[i] == int(argument):
			return fibonacci[i - 1]
		if fibonacci[i] != argument and fibonacci[i] > int(argument):
			return -1

def main():
	# 1. Handling Errors
	check_empty(sys.argv[1:])
	int_check(sys.argv[1])

	#2. Parsing
	fibonacci = [0, 1]
	argument = int(sys.argv[1])

	# 3. Resolution
	generate_fibonacci(argument, fibonacci)
	result = return_previous(argument, fibonacci)

	# 4. Display
	print(result)

if __name__ == "__main__":
	main()