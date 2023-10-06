#!/usr/bin/env python3

# Exercise 9. Chiffres Only = Digits only

import argparse

def is_int(value):
    try:
        int(value)
        return True
    except ValueError:
    	return False
        
def parse_arguments():
	parser = argparse.ArgumentParser(description='Check if our sting is made of number.')
	parser.add_argument('number_string', type=is_int, help='The string to check.')
	args = parser.parse_args()
	return args.number_string

def main():
	#1 and #2 and #3. Handling errors, Parsing and Resolution
	number_string = parse_arguments()

	# 4. Display
	print(number_string)

if __name__ == "__main__":
	main()
