# Python Crash Course pg 63 - Chapter 4: Copying a list
# Mogis 17 June 2021

my_foods = ['pizza', 'falafel', 'carrot cake']

# This slice creates a copy of the list in its original form, which will be edited below by the append commands to prove they're two distinct lists
friend_foods = my_foods[:]


my_foods.append('cannoli')
friend_foods.append('ice cream')


print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)

