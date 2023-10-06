#!/usr/bin/env python3

# Exercise 2. Combinaison de 2 nombres (Sorted combinations of 2 numbers in ascending order)

def find_sorted_combinations(a, b, sorted_combinations):
	while a < 99: # first number will be 98 max
		while b < 100: # second number will be 99 max
			if a < 10 and b > 9:
				sorted_combinations.append(f"0{a} {b}")
			elif b < 10 and a > 9:
				sorted_combinations.append(f"{a} 0{b}")
			elif b < 10 and a < 10:
				sorted_combinations.append(f"0{a} 0{b}")
			else:
				sorted_combinations.append(f"{a} {b}")
			b += 1 # increment second number
		a += 1 # increment first number
		b = a + 1 # reset second number
	return sorted_combinations

	
# 1. Handlin Errors 
# no need

# 2. Parsing 
sorted_combinations = []
# we start from the first possible combination 
first_num = 0 # first number of the combination
second_num = 1 # second number of the combination

# 3. Resolution

sorted_combinations = find_sorted_combinations(first_num, second_num, sorted_combinations)

# 4. Display 
print(*sorted_combinations, sep=", ")
