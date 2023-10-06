#!/usr/bin/env python3

# Exercise 11. Index Wanted

import argparse

def parse_arguments():
	parser = argparse.ArgumentParser(description='Process an arbitrary number of arguments.')
	parser.add_argument('inputs', nargs='+', help='Input arguments.')
	args = parser.parse_args()
	return args.inputs

def is_in_arguments_list(arguments):
	item_to_check = arguments[-1]
	for element in arguments[0:-1]:
		if element == item_to_check:
			return arguments.index(element)
	else:
		return -1
	
def main():
	#1 and #2. Handling errors and Parsing
	arguments = parse_arguments()

	# 3. Resolution
	is_in_argument = is_in_arguments_list(arguments)

	# 4. Display
	print(is_in_argument)

if __name__ == "__main__":
	main()
