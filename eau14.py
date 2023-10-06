#!/usr/bin/env python3

# Exercise 15. Par ordre ASCII = Sort in ASCII order
 
import argparse
import string

def is_str(value):
    try:
        int(value)
        raise argparse.ArgumentTypeError("error, arguments must a string.")
    except ValueError:
    	return value

def parse_arguments():
	parser = argparse.ArgumentParser(description='Process an arbitrary number of arguments.')
	parser.add_argument('inputs', nargs='+', type=is_str, help='Input arguments.')
	args = parser.parse_args()
	return args.inputs 


# we utilise the sorting algorythm method, by identifying the smallest element in each loop around our list
def sorted_arguments(arguments, letter_to_number): 
	lenght = len(arguments)
	for i in range(0, lenght - 1):
		min = i
		for j in range(i + 1, lenght): # we iteratre from i + 1 so that we don't iterate through the smallet value that we have identified in the previous round
			if letter_to_number[arguments[j][0]] < letter_to_number[arguments[min][0]]: #Note: we could have used the built in ord()function
				min = j
		if min != i:
			arguments[i], arguments[min] = arguments[min], arguments[i]
	return arguments

def main():
	#1 and #2. Handling errors and Parsing
	arguments = parse_arguments()
	# we generate this alphabet dictionnary to determine the order of the first charater of each argument. 
	letter_to_number = {letter: index+1 for index, letter in enumerate(string.ascii_lowercase + string.ascii_uppercase)} 

	# 3. Resolution
	ascii_sorted = sorted_arguments(arguments, letter_to_number)

	# 4. Display
	print(*ascii_sorted, sep=" ")
	
if __name__ == "__main__":
	main()
