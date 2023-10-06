#!/usr/bin/env python3

# Exercise 6. String in String

import argparse

def parse_str(value):
    try:
        return str(value)
    except ValueError:
        raise argparse.ArgumentTypeError("error.")

def parse_arguments():
	parser = argparse.ArgumentParser(description='Process two strings to check wether the second one is included in the first one or not.')
	parser.add_argument('big_string', type=parse_str, help='The first string.')
	parser.add_argument('small_string', type=parse_str, help='The second string.')
	args = parser.parse_args()
	return args.big_string, args.small_string

def generate_string_variations(big_string_variations, big_string, small_string):
	i = 0 # index incrementor
	small_string_length = len(small_string)
	while len(big_string[i:]) >= small_string_length:
		big_string_variations.append(big_string[i:i + small_string_length])
		i += 1
	return(big_string_variations)

def is_small_string_in_big_string(big_string_variations, small_string):
	for string in big_string_variations:
		if string == small_string:
			return True
	else:
		return False

def main():

	#1 and #2. Handling errors and Parsing
	big_string_variations = []
	big_string, small_string = parse_arguments()

	# 3. Resolution
	generate_string_variations(big_string_variations, big_string, small_string)
	outcome = is_small_string_in_big_string(big_string_variations, small_string)

	# 4. Display
	print(outcome)

if __name__ == "__main__":
	main()
