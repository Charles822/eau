#!/usr/bin/env python3

# Exercise 12. Difference Minimum Absolue (Absolute minimum gap between numbers)

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

def minimum_gap(arguments):
	sorted_arguments = sorted(arguments)
	gaps = []
	for element in sorted_arguments[0:-1]:
		next_number = sorted_arguments[sorted_arguments.index(element) + 1]
		gaps.append(next_number - element)
	return min(gaps)

def main():
	#1 and #2. Handling errors and Parsing
	arguments = parse_arguments()

	# 3. Resolution
	minimum_difference = minimum_gap(arguments)

	# 4. Display
	print(minimum_difference)

if __name__ == "__main__":
	main()
