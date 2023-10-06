#!/usr/bin/env python3

# Exercise 8. Majuscule = Every word of my string must start with an uppercase 

import argparse

def not_int(value):
    try:
        int(value)
        raise argparse.ArgumentTypeError("Cannot be an interger.")
    except ValueError:
    	return value
        
def parse_arguments():
	parser = argparse.ArgumentParser(description='Process a string to return it with an uppercase at the begining of each word .')
	parser.add_argument('normal_string', type=not_int, help='The string you want to convert.')
	args = parser.parse_args()
	return args.normal_string

# add an uppercase letter at the begining of each word
def add_uppercase_first_letters(normal_string, space): 
	normal_string = normal_string.lower() 
	converted_string = ""
	converted_string += normal_string[0].upper() # the first character of our string must start with an uppercase
	cap_trigger = False # cap_trigger is triggered, the next letter will be converted to uppercase
	for char in normal_string[1:]:
		if char in space:
			converted_string += char
			cap_trigger = True
		elif cap_trigger == True:	
			converted_string += char.upper()
			cap_trigger = False
		else:
			converted_string += char
	return converted_string

def main():
	#1 and #2. Handling errors and Parsing
	normal_string = parse_arguments()

	# 3. Resolution
	space = " \n\t"
	converted_string = add_uppercase_first_letters(normal_string, space)
	
	# 4. Display
	print(converted_string)


if __name__ == "__main__":
	main()
