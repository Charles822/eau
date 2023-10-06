#!/usr/bin/env python3

# Exercise 1. Combinaison de 3 chiffres (Sorted combinations of 3 numbers in ascending order)

def find_sorted_combinations(a, b, c, sorted_combinations):
	while a < b < c:
		if c > 9: 
			b += 1
			c = b + 1
		if b > 8: 
			a += 1
			b = a + 1
			c = b + 1
		if a > 7: 
			return sorted_combinations
		sorted_combinations.append(f"{a}{b}{c}")
		c +=1
	
# 1. Handlin Errors 
# no need

# 2. Parsing 
sorted_combinations = []

# we start from the first possible combination 
first_num = 0 # first number of the combination
second_num = 1 # second number of the combination
third_num = 2 # third number of the combination

# 3. Resolution

sorted_combinations = find_sorted_combinations(first_num, second_num, third_num, sorted_combinations)

# 4. Display 
print(*sorted_combinations, sep=", ")
