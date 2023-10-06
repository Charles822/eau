#!/usr/bin/env python3

# Exercise 7. Majuscule sur 2 = Convert letters in a string in uppercase every 2 letters

import argparse

import string

def not_int(value):
    try:
        int(value)
        raise argparse.ArgumentTypeError("Cannot be an interger.")
    except ValueError:
    	return value
        
def parse_arguments():
	parser = argparse.ArgumentParser(description='Process a string and return it with a upper cap every 2 letters.')
	parser.add_argument('normal_string', type=not_int, help='The string you want to convert.')
	args = parser.parse_args()
	return args.normal_string

def convert_into_upper(normal_string, letters):
	converted_string = ""
	converter_count = 0 # we set a converter count to build the logic where we convert in uppercase every 2 letters
	# we convert only if the converter count is an even number and belong to a - z 
	for char in normal_string:
		if char in letters and converter_count % 2 == 0: 
			converted_string += char.upper()
			converter_count += 1
		elif char in letters and converter_count % 2 != 0:
			converted_string += char
			converter_count += 1
		else:
			converted_string += char
	return converted_string 

def main():

	#1 and #2. Handling errors and Parsing
	normal_string = parse_arguments()

	# 3. Resolution
	letters = string.ascii_letters
	converted_string = convert_into_upper(normal_string, letters)
	
	# 4. Display
	print (converted_string)


if __name__ == "__main__":
	main()
