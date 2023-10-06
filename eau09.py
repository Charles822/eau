#!/usr/bin/env python3

# Exercise 10: Entre Min et Max (between min and max)

import argparse

def is_int(value):
    try:
        return int(value)
    except ValueError:
        raise argparse.ArgumentTypeError("error, arguments must be convertible into an integer.")

def parse_arguments():
	parser = argparse.ArgumentParser(description='Process two strings to check wether the second one is included in the first one or not.')
	parser.add_argument('first_num', type=is_int, help='The first number.')
	parser.add_argument('second_num', type=is_int, help='The second number.')
	args = parser.parse_args()
	return args.first_num, args.second_num

def min_to_max(first_num, second_num):
	min_to_max = []
	if first_num > second_num: 
		for num in range(second_num, first_num):
			min_to_max.append(num)
	elif second_num > first_num:
		for num in range(first_num, second_num):
			min_to_max.append(num)
	return min_to_max
	
def main():
	#1 and #2. Handling errors and Parsing
	first_num, second_num = parse_arguments()

	# 3. Resolution
	ascendant_numbers = min_to_max(first_num, second_num)

	# 4. Display
	print(*ascendant_numbers, sep=" ")

if __name__ == "__main__":
	main()
