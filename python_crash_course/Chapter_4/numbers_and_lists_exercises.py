# Python Crash Course pg 60 - Chapter 4: Lists
# Mogis 16 June 2021

'''
# Exercise 4-3: Use a for loop to print the numbers from 1 to 20, inclusive

for value in range(1, 21):
	print(value)
'''
#---------------------------------------------------------------------------------------
'''
# Exercise 4-4: Make a list of the numbers from one to one million, and then use a for loop to print the numbers...my laptop is about to explode

million = []

for value in range(1, 1000001):
	number = value
	million.append(value)

print(million)
# That actually didn't turn out so badly....wow
'''
#---------------------------------------------------------------------------------------
'''
# Exercise 4-5: Make a list of the numbers one to one million, and then use min() and max() to make sure your list actually starts at one and ends at one million.
# Also, use the sum() function to see how quickly Python can add a million numbers

million = []

for value in range(1, 1000001):
	number = value
	million.append(value)

minimum = min(million)
print(minimum)

maximum = max(million)
print(maximum)

total = sum(million)
print(total)
'''
#---------------------------------------------------------------------------------------
'''
# Exercise 4-6: Use the third argument of the range() function to make a list of the odd numbers from 1 to 20. Use a for loop to print each number

odds = []

for value in range(1, 20, 2):
	print(value)
'''
#---------------------------------------------------------------------------------------
'''
# Exercise 4-7: Make a list of the multiples of 3 from 3 to 30. Use a for loop to print the numbers in your list.

multiples_of_3 = []

for value in range(3, 31, 3):
	print(value)
'''
#---------------------------------------------------------------------------------------
'''
# Exercise 4-8: A number raised to the third power is called a cube. For example the cube of 2 is written as 2**3 in Python. Make a list of the first 10 cubes
# and use a for loop to print out the value of each cube.

for value in range(1, 11):
	value = value**3
	print(value)
'''
#---------------------------------------------------------------------------------------

# Exercise 4-9: Use a list comprehension to generate a list of the first 10 cubes.

cubes = [value**3 for value in range(1,11)]
print(cubes)