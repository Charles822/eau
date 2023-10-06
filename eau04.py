#!/usr/bin/env python3

# Exercise 5. Prochain Nombre Premier (next prime number)

import argparse

def generate_list(argument, prime_list): # generate all numbers between our argument and the biggest gap between 2 prime numbers 
	for num in range(argument, argument + 246):
		prime_list.append(num)
	return prime_list


def remove_non_prime(prime_list): # remove non prime numbers from our default list to get a clean list with prime numbers only
	for num in prime_list.copy():  
		for a in range(2, num):
			try:
				if num % a == 0:
					prime_list.remove(num)
			except ValueError:
					pass
	return prime_list

def get_next_prime_number(argument, prime_list):
	for num in prime_list:
		if num > argument:
			return num

def parse_arguments():
    # Parse the command line arguments.
    parser = argparse.ArgumentParser(description='Generate the next prime number.')
    parser.add_argument('num', type=parse_int, help='The number to start generating primes from.') # use parse_int to return a custom error message
    args = parser.parse_args()
    if args.num < 0:
        print(-1)
        exit()
    return args.num
 
def parse_int(value): # custome function to print -1 if the type of the argument is not and integer
    try:
        return int(value)
    except ValueError:
        raise argparse.ArgumentTypeError(-1)

def main():

	#1 and #2. Handling errors and Parsing
	prime_list = []
	argument = parse_arguments()

	# 3. Resolution
	generate_list(argument, prime_list)
	remove_non_prime(prime_list)
	next_prime_number = get_next_prime_number(argument, prime_list)

	# 4. Display
	print(next_prime_number)

if __name__ == "__main__":
	main()