# This code is for chapter 3 (Lists) of Python Crash Course - page 43
# Blake Barrow / 14 June 2021

'''
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
# The sort command alphabetizes the list
cars.sort()

print(cars)

# Using the reverse=true property for sort() allows the list to be alphabetized from Z to A
cars.sort(reverse=True)
print(cars)
#-----------------------------------------------------------------------------


cars = ['bmw', 'audi', 'toyota', 'subaru']

print('"Here is the original list:')
print(cars)

print('\nHere is the sorted list:')
print(sorted(cars))

print('\nHere is the original list again:')
print(cars)

'''
#-----------------------------------------------------------------------------

cars = ['bmw', 'audi', 'toyota', 'subaru']

print(cars)

cars.reverse()
print(cars)

print('How many cars have I put in this list? Let us use the len() command to find out!')
len(cars)
print(len(cars))
