#!/usr/bin/env python3

# Exercise 13. Tri à bulle = Bubble Sort

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
	for i in range(len(arguments), 1, -1):
		for j in range(0, i - 1):
			pos1 = j # position of the first number to compare
			pos2 = j + 1 # position of the second number to compare
			if arguments[pos2] < arguments[pos1]: # logic to swap them
				arguments[pos1], arguments[pos2] = arguments[pos2], arguments[pos1] 
	return arguments

def main():
	#1 and #2. Handling errors and Parsing
	arguments = parse_arguments()

	# 3. Resolution
	bubble_sort = sorted_arguments(arguments)

	# 4. Display
	print(*bubble_sort, sep=" ")
	
if __name__ == "__main__":
	main()
