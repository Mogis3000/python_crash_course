'''
squares = []
for value in range(1, 11):
	square = value ** 2
	squares.append(square)

print(squares)

'''

squares = []
for value in range(1,11):
	squares.append(value ** 2)

print(squares)

#---------------------------------------------------------------------------------------
'''
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(min(digits))

print(max(digits))

print(sum(digits))
'''
#---------------------------------------------------------------------------------------
# This code will reproduce the same effect as the top section of code, but this uses a technique called list comprehension, it's slightly more advanced but very common.
# List comprehension is a code shortening technique that allows someone to remove the need for a variable that can be used to modify a list within the same step.
squares = [value**2 for value in range(1, 11)]
print(squares)