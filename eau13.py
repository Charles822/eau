#!/usr/bin/env python3

# Exercise 14. Tri par sélection = Sorting Algorithm 

import argparse

def is_int(value):
    try:
        return int(value)
    except ValueError:
        raise argparse.ArgumentTypeError("error, arguments must be convertible into an integer.")

def parse_arguments():
	parser = argparse.ArgumentParser(description='Process an arbitrary number of arguments.')
	parser.add_argument('inputs', nargs='+', type=is_int, help='Input arguments.')
	args = parser.parse_args()
	return args.inputs 

def sorted_arguments(arguments):
	lenght = len(arguments)
	for i in range(0, lenght - 1):
		min = i
		for j in range(i + 1, lenght):
			if arguments[j] < arguments[min]:
				min = j
		if min != i:
			arguments[i], arguments[min] = arguments[min], arguments[i]
	return arguments
	
def main():
	#1 and #2. Handling errors and Parsing
	arguments = parse_arguments()

	# 3. Resolution
	sorting_algo = sorted_arguments(arguments)

	# 4. Display
	print(*sorting_algo, sep=" ")
	
if __name__ == "__main__":
	main()
