# Python Crash Course - Chapter 4, pg 50, working with lists

# Create a list that has multiple values
magicians = ['alice', 'david', 'carlina']

# create a for loop that prints the names of the magician
for magician in magicians:
	print(magician)


# Create a for loop that prints a message to the magician
for magician in magicians:
	print(f'{magician.title()}, that was a great magic trick!')
	print(f"I can't wait to see your next one, {magician.title()}!\n")

print("Thank you everyone, that was a great magic show!")


'''
# Create a for loop that makes an indentation error
for magician in magicians:
print(magician)
'''

'''
# Create a for loop that makes a syntax error. This loop is missing the : in the first line
for magician in magicians
	print(magician)
'''

