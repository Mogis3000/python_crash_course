# Python Crash Course Ch 4 - pg 58: Using range and numbers with lists
# Blake Barrow 16 June 2021

# the range() command uses 2 arguments to annotate a starting number and an ending number. The end number is NOT included in the range, so 1,6 will display numbers 1-5
for value in range(1, 6):
	print(value)


numbers = list(range(1, 6))
print(numbers)
